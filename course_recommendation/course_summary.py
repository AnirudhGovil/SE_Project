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
        with open('data_generation/course_features_aggregated.pkl', 'rb') as file:
            course_features_aggregated = pickle.load(file)
        return course_features_aggregated

def load_courses():
    """
    Loads the json file containing course information.
    
    Returns:
    - courses: A dictionary containing course information, with course IDs as keys.
    """
    with open('data_generation/courses.json', 'r') as file:
        courses = json.load(file)
    return courses

def load_course_feedbacks():
    """
    Loads the json file containing course feedbacks.
    
    Returns:
    - feedbacks: A list of feedbacks.
    """
    with open('data_generation/course_feedbacks.json', 'r') as file:
        feedbacks = json.load(file)
    return feedbacks

def load_course_prompt(code, courses, course_features_aggregated, feedbacks):
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
    
    # Feedbacks
    feedback = ""
    for i, f in enumerate(feedbacks):
        feedback += f'"{i+1}": "{f}",\n'
    
    prompt = []
    prompt.append({
        "role": "system",
        "content": f"""You are an expert in sentiment analyses and course feedbacks. Given the below details of the course along with feedbacks from students, generate a summary giving information about the course. The summary should include all the points mentioned in the feedbacks and deduce a description of the courses based on that.
        
        The format shoud be like this:
        Summary: <summary>
        You should take the course if: <reasons>
        You should not take the course if: <reasons>
        """})
    prompt.append({
        "role": "user",
        "content": f"""Course Name: {course_info['Name']},
        Questions: {qna},
        Feedbacks: {feedback}
        """
    })
    
    return prompt

def get_summary(generator, dialogs, max_gen_len, temperature, top_p):
    results = generator.chat_completion(
        dialogs,
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
    
    summaries = []
    for dialog, result in zip(dialogs, results):
        summaries.append(result['generation']['content'])
    return summaries

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
    courses = load_courses()
    course_feat = load_course_features()
    feedbacks = load_course_feedbacks()
    
    prompts = []
    for course_code in feedbacks.keys():
        prompt = load_course_prompt(course_code, courses, course_feat, feedbacks[course_code])
        prompts.append(prompt)
    
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    
    dialogs: List[Dialog] = prompts

    # results = generator.chat_completion(
    #     dialogs,
    #     max_gen_len=max_gen_len,
    #     temperature=temperature,
    #     top_p=top_p,
    # )
    # for dialog, result in zip(dialogs, results):
    #     for msg in dialog:
    #         print(f"{msg['role'].capitalize()}: {msg['content']}\n")
    #     print(
    #         f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
    #     )
    #     print("\n==================================\n")
    course_summaries = {}
    from tqdm import tqdm
    for i in tqdm(range(0, len(dialogs), 2)):
        summaries = get_summary(generator, dialogs[i:i+2], max_gen_len, temperature, top_p)
        for j in range(len(summaries)):
            # print(f"Course: {courses[i+j]['Name']}")
            # print(f"Summary: {summaries[j]}")
            # print("==================================\n")
            course_summaries[courses[i+j]['ID']] = summaries[j]
    
    with open('data_generation/course_summaries.json', 'w') as file:
        json.dump(course_summaries, file, indent=4)

if __name__ == "__main__":
    fire.Fire(main)