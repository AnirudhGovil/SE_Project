import sqlite3
from dataclasses import dataclass
from backend.DTO.courseStudentDTO import CourseStudentDTO
db_path = "backend/Database/Course.db"

import sqlite3

class CourseStudentDAO:
    def __init__(self):
        self.db_path = db_path

    def create_course_student(self, course_student_dto):
        """
        Adds a new course-student relationship to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
            c = conn.cursor()
            c.execute("INSERT INTO CourseStudents (course_id, student_id) VALUES (?, ?)",
                      (course_student_dto.course_id, course_student_dto.student_id))
            conn.commit()
        finally:
            conn.close()

    def read_course_student(self, course_id, student_id):
        """
        Retrieves a specific course-student relationship from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT course_id, student_id FROM CourseStudents WHERE course_id = ? AND student_id = ?",
                  (course_id, student_id))
        result = c.fetchone()
        conn.close()
        if result:
            return CourseStudentDTO(*result)
        return None

    def update_course_student(self, original_course_id, original_student_id, new_course_id, new_student_id):
        """
        Updates a course-student relationship in the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("UPDATE CourseStudents SET course_id = ?, student_id = ? WHERE course_id = ? AND student_id = ?",
                  (new_course_id, new_student_id, original_course_id, original_student_id))
        conn.commit()
        conn.close()

    def delete_course_student(self, course_id, student_id):
        """
        Deletes a course-student relationship from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("DELETE FROM CourseStudents WHERE course_id = ? AND student_id = ?",
                  (course_id, student_id))
        conn.commit()
        conn.close()

    def find_courses_by_student(self, student_id):
        """
        Returns a list of all courses taken by a specific student.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT course_id FROM CourseStudents WHERE student_id = ?", (student_id,))
        courses = c.fetchall()
        conn.close()
        return [course[0] for course in courses]  # Returning only course IDs for simplicity

    def find_students_by_course(self, course_id):
        """
        Returns a list of all students in a specific course.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT student_id FROM CourseStudents WHERE course_id = ?", (course_id,))
        students = c.fetchall()
        conn.close()
        return [student[0] for student in students]  # Returning only student IDs for simplicity

# Example Usage
if __name__ == "__main__":
    dao = CourseStudentDAO()
    
    dao.delete_course_student(1, 1)

    # Create a new course-student relationship
    new_course_student = CourseStudentDTO(course_id=1, student_id=1)
    dao.create_course_student(new_course_student)

    # Read a course-student relationship
    course_student = dao.read_course_student(1, 1)
    print(course_student)

    # Update a course-student relationship
    dao.update_course_student(1, 1, 2, 200)

    # Read the updated course-student relationship
    course_student = dao.read_course_student(2, 200)
    print(course_student)    

    # Get all courses by a specific student
    courses_by_student = dao.find_courses_by_student(200)
    print(courses_by_student)

    # Get all students in a specific course
    students_by_course = dao.find_students_by_course(2)
    print(students_by_course)

    # Delete a course-student relationship
    dao.delete_course_student(2, 200)

    # Read a course-student relationship
    course_student = dao.read_course_student(2, 200)
    print(course_student)
