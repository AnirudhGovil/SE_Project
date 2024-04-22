import sqlite3
from dataclasses import dataclass
from backend.DTO.courseDTO import CourseDTO
db_path = "backend/Database/Course.db"


class CourseDAO:
    def __init__(self):
        self.db_path = db_path

    def create_course(self, course_dto):
        """
        Adds a new course to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
            c = conn.cursor()
            c.execute("INSERT INTO Courses (course_id, name, session, instructor_id) VALUES (?, ?, ?, ?)",
                      (course_dto.course_id, course_dto.name, course_dto.session, course_dto.instructor_id))
            conn.commit()
        finally:
            conn.close()

    def read_course(self, course_id):
        """
        Retrieves a course's details from the database by course ID.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT course_id, name, session, instructor_id FROM Courses WHERE course_id = ?", (course_id,))
        result = c.fetchone()
        conn.close()
        if result:
            return CourseDTO(*result)
        return None

    def update_course(self, course_dto):
        """
        Updates a course's details in the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("UPDATE Courses SET name = ?, session = ?, instructor_id = ? WHERE course_id = ?",
                  (course_dto.name, course_dto.session, course_dto.instructor_id, course_dto.course_id))
        conn.commit()
        conn.close()

    def delete_course(self, course_id):
        """
        Deletes a course from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("DELETE FROM Courses WHERE course_id = ?", (course_id,))
        conn.commit()
        conn.close()

    def find_courses_by_instructor(self, instructor_id):
        """
        Returns a list of all courses taught by a specific instructor.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT course_id, name, session, instructor_id FROM Courses WHERE instructor_id = ?", (instructor_id,))
        results = c.fetchall()
        conn.close()
        return [CourseDTO(*row) for row in results]

    def find_courses_by_session(self, session):
        """
        Returns a list of all courses in a specific session.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT course_id, name, session, instructor_id FROM Courses WHERE session = ?", (session,))
        results = c.fetchall()
        conn.close()
        return [CourseDTO(*row) for row in results]

# Example Usage
if __name__ == "__main__":
    dao = CourseDAO()
    
    # Create a new course
    new_course = CourseDTO(course_id=1, name='Introduction to Python', session='Fall 2023', instructor_id=3)
    dao.create_course(new_course)

    # Read a course's details
    course = dao.read_course(1)
    print(course)

    # Update a course's details
    updated_course = CourseDTO(course_id=1, name='Advanced Python', session='Spring 2024', instructor_id=3)
    dao.update_course(updated_course)

    # Read the updated course's details
    course = dao.read_course(1)
    print(f'updated: {course}')

    # Get all courses by a specific instructor
    courses_by_instructor = dao.find_courses_by_instructor(3)
    print(f'courses by instructor: {courses_by_instructor}')

    # Get all courses by session
    courses_by_session = dao.find_courses_by_session('Spring 2024')
    print(f'courses by session: {courses_by_session}')

    # # Delete a course
    # dao.delete_course(1)

    # # Read a course's details
    # course = dao.read_course(1)
    # print(course)