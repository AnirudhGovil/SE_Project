from dataclasses import dataclass


@dataclass
class FeedbackDTO:
    feedback_id: int
    course_id: int
    student_id: int
    feedback_text: str
