from dataclasses import dataclass


@dataclass
class RatingDTO:
    rating_id: int
    course_id: int
    student_id: int
    rating_value: int