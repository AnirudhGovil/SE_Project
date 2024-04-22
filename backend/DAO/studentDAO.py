import sqlite3
from dataclasses import dataclass
from backend.DTO.studentDTO import StudentDTO
db_path = "backend/Database/Course.db"


class StudentDAO:
    def __init__(self):
        self.db_path = db_path

    def create_student(self, student_dto):
        """
        Adds a new student to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
            c = conn.cursor()
            c.execute("INSERT INTO Students (student_id, name, email, roll_number) VALUES (?, ?, ?, ?)",
                      (student_dto.student_id, student_dto.name, student_dto.email, student_dto.roll_number))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
        return True

    def read_student(self, student_id):
        """
        Retrieves a student's details from the database by student ID.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT student_id, name, email, roll_number FROM Students WHERE student_id = ?", (student_id,))
        result = c.fetchone()
        conn.close()
        if result:
            return StudentDTO(*result)
        return None

    def update_student(self, student_dto):
        """
        Updates a student's details in the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("UPDATE Students SET name = ?, email = ?, roll_number = ? WHERE student_id = ?",
                  (student_dto.name, student_dto.email, student_dto.roll_number, student_dto.student_id))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0

    def delete_student(self, student_id):
        """
        Deletes a student from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("DELETE FROM Students WHERE student_id = ?", (student_id,))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0

# Example Usage
if __name__ == "__main__":
    dao = StudentDAO()
    
    # Create a new student
    new_student = StudentDTO(student_id=1, name='John Doe', email='johndoe@example.com', roll_number=101)
    dao.create_student(new_student)

    # Read a student's details
    student = dao.read_student(1)
    print(student)

    # Update a student's details
    updated_student = StudentDTO(student_id=1, name='Johnny Doe', email='johnnydoe@example.com', roll_number=102)
    dao.update_student(updated_student)

    # Read the updated student's details
    student = dao.read_student(1)
    print(f'updated: {student}')

    # # Delete a student
    # dao.delete_student(1)

    # # Read a student's details
    # student = dao.read_student(1)
    # print(student)

