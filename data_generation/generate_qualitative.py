# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

from typing import List, Optional

import fire

from llama import Dialog, Llama

import pickle
import numpy as np
import json

def load_course_features():
        """
        Loads the aggregated course features from a pickle file.

        Returns:
        - course_features_aggregated: A dictionary containing aggregated course features, with course IDs as keys.
        """
        with open('course_features_aggregated.pkl', 'rb') as file:
            course_features_aggregated = pickle.load(file)
        return course_features_aggregated

def load_courses():
    """
    Loads the json file containing course information.
    
    Returns:
    - courses: A dictionary containing course information, with course IDs as keys.
    """
    with open('courses.json', 'r') as file:
        courses = json.load(file)
    return courses

def load_course_prompt(code, courses, course_features_aggregated):
    """
    Loads the course prompt for the given course code from a json file.

    Args:
    - code: The course code for which the prompt is to be loaded.

    Returns:
    - prompt: The course prompt for the given course code.
    """
    common_questions = [
        "How would you rate the difficulty of the course?",
        "How would you rate the extent of time commitment required for the course?",
        "How well do you think the course was structured?",
        "How would you rate the quality of the course material?",
        "How would you rate the quality of the assignments?",
        "How would you rate the quality of the exams?",
        "How well did the course align with your expectations?",
        "How likely are you to this course to your juniors?",
    ]
    
    course_features = course_features_aggregated[code]
    course_info = {}
    for course in courses:
        if course['ID'] == code:
            course_info = course
            break    
    for questions in course_info['Questions']:
        common_questions.append(questions)
    
    qna = ""
    for q,a in zip(common_questions, course_features):
        # round the answer to 2 decimal places
        qna += f'"{q}": {round(a, 2)},\n'
    # print(qna)
    prompt = []
    prompt.append({
        "role": "system",
        "content": f"""You are an expert in sentiment analyses and course feedbacks. You need to generate 10 possible course feedbacks that students could give for a course that will be given by the user. All questions are out of 10. Write a paragraph for each feedback. Do not mention any sort of score in the feedback as those have already been provided in the questions, rather focus on more abstract things that a student might want to highlight about the course, instructor, material etc. Make sure that the students give a good feedback for topics whose scores are > 7 and negative feedback for topics whose scores are < 5.
        
        The format should just be:
        Feedback Number: A paragraph of feedback.
        """})
    prompt.append({
        "role": "user",
        "content": f"""Course Name: {course_info['Name']},Questions: {qna}"""
    })
    
    return prompt


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 4,
    max_gen_len: Optional[int] = None,
):
    """
    Examples to run with the models finetuned for chat. Prompts correspond of chat
    turns between the user and assistant with the final one always being the user.

    An optional system prompt at the beginning to control how the model should respond
    is also supported.

    The context window of llama3 models is 8192 tokens, so `max_seq_len` needs to be <= 8192.

    `max_gen_len` is optional because finetuned models are able to stop generations naturally.
    """
    courses = load_courses()[:2]
    course_feat = load_course_features()
    prompts = []
    for course in courses:
        course_code = course['ID']
        prompt = load_course_prompt(course_code, courses, course_feat)
        prompts.append(prompt)
    # print(prompts)
    # exit()
    
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    
    dialogs: List[Dialog] = prompts
    # dialogs: List[Dialog] = [
    #     [{
    #         "role": "user", 
    #         "content": """
    #         what is the general sentiment of this review? Note the ratings are out of 10 and the general bounds of a good course is > 7.
            
    #         "MA22053": {
    #         "How would you rate the difficulty of the course?": 5,
    #         "How would you rate the extent of time commitment required for the course?": 5,
    #         "How much would you say you learned from the course?": 5,
    #         "How well do you think the course was structured?": 5,
    #         "How would you rate the quality of the course material?": 5,
    #         "How would you rate the quality of the assignments?": 5,
    #         "How would you rate the quality of the exams?": 5,
    #         "How well did the course align with your expectations?": 4,
    #         "How likely are you to recommend this course to your juniors?": 6,
    #         "How well did the course cover topics such as logic, sets, functions, and combinatorics?": 4,
    #         "To what extent did the course provide insights into applications of discrete mathematics in computer science and cryptography?": 3,
    #         "How useful were the assignments and problem-solving exercises in understanding discrete mathematics concepts?": 7}
    #         """}],
    # ]
    results = generator.chat_completion(
        dialogs,
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    for dialog, result in zip(dialogs, results):
        for msg in dialog:
            print(f"{msg['role'].capitalize()}: {msg['content']}\n")
        print(
            f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
        )
        # print(result['generation']['content'])
        print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)
