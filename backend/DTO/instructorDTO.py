from dataclasses import dataclass

@dataclass
class InstructorDTO:
    instructor_id: int
    name: str
    email: str