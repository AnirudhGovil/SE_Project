from dataclasses import dataclass


@dataclass
class CourseDTO:
    course_id: int
    name: str
    session: str
    instructor_id: int