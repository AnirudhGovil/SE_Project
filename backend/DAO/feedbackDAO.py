import sqlite3
from dataclasses import dataclass
from backend.DTO.feedbackDTO import FeedbackDTO
db_path = "backend/Database/Course.db"


class FeedbackDAO:
    def __init__(self):
        self.db_path = db_path

    def create_feedback(self, feedback_dto):
        """
        Adds a new feedback to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
            c = conn.cursor()
            c.execute("INSERT INTO Feedback (feedback_id, course_id, student_id, feedback_text) VALUES (?, ?, ?, ?)",
                    (feedback_dto.feedback_id, feedback_dto.course_id, feedback_dto.student_id, feedback_dto.feedback_text))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
        return True

    def read_feedback(self, feedback_id):
        """
        Retrieves a feedback's details from the database by feedback ID.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT feedback_id, course_id, student_id, feedback_text FROM Feedback WHERE feedback_id = ?",
                  (feedback_id,))
        result = c.fetchone()
        conn.close()
        if result:
            return FeedbackDTO(*result)
        return None

    def update_feedback(self, feedback_dto):
        """
        Updates a feedback's details in the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("UPDATE Feedback SET course_id = ?, student_id = ?, feedback_text = ? WHERE feedback_id = ?",
                  (feedback_dto.course_id, feedback_dto.student_id, feedback_dto.feedback_text, feedback_dto.feedback_id))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0

    def delete_feedback(self, feedback_id):
        """
        Deletes a feedback from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("DELETE FROM Feedback WHERE feedback_id = ?", (feedback_id,))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0

    def list_feedback_by_course(self, course_id):
        """
        Returns all feedback entries for a specific course.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT * FROM Feedback WHERE course_id = ?", (course_id,))
        results = c.fetchall()
        conn.close()
        return [FeedbackDTO(*row) for row in results]

    def list_feedback_by_student(self, student_id):
        """
        Returns all feedback entries made by a specific student.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT * FROM Feedback WHERE student_id = ?", (student_id,))
        results = c.fetchall()
        conn.close()
        return [FeedbackDTO(*row) for row in results]

# Example Usage
if __name__ == "__main__":
    dao = FeedbackDAO()
    
    # Create a new feedback
    new_feedback = FeedbackDTO(feedback_id=1, course_id=1, student_id=1, feedback_text="Very informative course.")
    dao.create_feedback(new_feedback)

    # Read a feedback's details
    feedback = dao.read_feedback(1)
    print(feedback)

    # Update a feedback's details
    updated_feedback = FeedbackDTO(feedback_id=1, course_id=1, student_id=1, feedback_text="Excellent course with great content.")
    dao.update_feedback(updated_feedback)

    # Read a feedback's details
    feedback = dao.read_feedback(1)
    print(f'updated: {feedback}')

    # List all feedback for a course
    feedbacks_course = dao.list_feedback_by_course(1)
    print(feedbacks_course)

    # List all feedback by a student
    feedbacks_student = dao.list_feedback_by_student(1)
    print(feedbacks_student)

    # Delete a feedback
    dao.delete_feedback(1)

    # Read a feedback's details
    feedback = dao.read_feedback(1)
    print(feedback)
