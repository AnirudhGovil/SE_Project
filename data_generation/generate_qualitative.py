# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

from typing import List, Optional

import fire

from llama import Dialog, Llama


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
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    dialogs: List[Dialog] = [
        [{
            "role": "user", 
            "content": """
            what is the general sentiment of this review? Note the ratings are out of 10 and the general bounds of a good course is > 7.
            
            "MA22053": {
            "How would you rate the difficulty of the course?": 5,
            "How would you rate the extent of time commitment required for the course?": 5,
            "How much would you say you learned from the course?": 5,
            "How well do you think the course was structured?": 5,
            "How would you rate the quality of the course material?": 5,
            "How would you rate the quality of the assignments?": 5,
            "How would you rate the quality of the exams?": 5,
            "How well did the course align with your expectations?": 4,
            "How likely are you to recommend this course to your juniors?": 6,
            "How well did the course cover topics such as logic, sets, functions, and combinatorics?": 4,
            "To what extent did the course provide insights into applications of discrete mathematics in computer science and cryptography?": 3,
            "How useful were the assignments and problem-solving exercises in understanding discrete mathematics concepts?": 7}
            """}],
    ]
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
        print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)
