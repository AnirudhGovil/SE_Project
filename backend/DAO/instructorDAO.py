import sqlite3
from dataclasses import dataclass
from backend.DTO.instructorDTO import InstructorDTO
db_path = "backend/Database/Course.db"


class InstructorDAO:
    def __init__(self):
        self.db_path = db_path

    def create_instructor(self, instructor_dto):
        """
        Adds a new instructor to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
            c.execute("INSERT INTO Instructors (instructor_id, name, email) VALUES (?, ?, ?)",
                      (instructor_dto.instructor_id, instructor_dto.name, instructor_dto.email))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
        return True

    def read_instructor(self, instructor_id):
        """
        Retrieves an instructor's details from the database by instructor ID.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT instructor_id, name, email FROM Instructors WHERE instructor_id = ?", (instructor_id,))
        result = c.fetchone()
        conn.close()
        if result:
            return InstructorDTO(*result)
        return None

    def update_instructor(self, instructor_dto):
        """
        Updates an instructor's details in the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("UPDATE Instructors SET name = ?, email = ? WHERE instructor_id = ?",
                  (instructor_dto.name, instructor_dto.email, instructor_dto.instructor_id))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0

    def delete_instructor(self, instructor_id):
        """
        Deletes an instructor from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("DELETE FROM Instructors WHERE instructor_id = ?", (instructor_id,))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0


# Example Usage
if __name__ == "__main__":
    dao = InstructorDAO()
    
    # Create a new instructor
    new_instructor = InstructorDTO(instructor_id=3, name='Jane Smith', email='janesmith@example.com')
    dao.create_instructor(new_instructor)

    # Read an instructor's details
    instructor = dao.read_instructor(3)
    print(instructor)

    # Update an instructor's details
    updated_instructor = InstructorDTO(instructor_id=3, name='Jane Doe', email='janedoe@example.com')
    num_changes = dao.update_instructor(updated_instructor)
    print(f'Number of changes: {num_changes}')

    # Read the updated instructor's details
    instructor = dao.read_instructor(3)
    print(f'updated: {instructor}')

    # Delete an instructor
    # dao.delete_instructor(3)

    # # Read an instructor's details
    # instructor = dao.read_instructor(3)
    # print(instructor)