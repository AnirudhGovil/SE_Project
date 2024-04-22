from dataclasses import dataclass


@dataclass
class StudentDTO:
    student_id: int
    name: str
    email: str
    roll_number: int