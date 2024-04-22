import sqlite3
from dataclasses import dataclass
from backend.DTO.ratingDTO import RatingDTO
db_path = "backend/Database/Course.db"


class RatingDAO:
    def __init__(self):
        self.db_path = db_path

    def create_rating(self, rating_dto):
        """
        Adds a new rating to the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("INSERT INTO Ratings (rating_id, course_id, student_id, rating_value) VALUES (?, ?, ?, ?)",
                  (rating_dto.rating_id, rating_dto.course_id, rating_dto.student_id, rating_dto.rating_value))
        conn.commit()
        conn.close()

    def read_rating(self, rating_id):
        """
        Retrieves a rating's details from the database by rating ID.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT rating_id, course_id, student_id, rating_value FROM Ratings WHERE rating_id = ?",
                  (rating_id,))
        result = c.fetchone()
        conn.close()
        if result:
            return RatingDTO(*result)
        return None

    def update_rating(self, rating_dto):
        """
        Updates a rating's details in the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("UPDATE Ratings SET course_id = ?, student_id = ?, rating_value = ? WHERE rating_id = ?",
                  (rating_dto.course_id, rating_dto.student_id, rating_dto.rating_value, rating_dto.rating_id))
        conn.commit()
        conn.close()

    def delete_rating(self, rating_id):
        """
        Deletes a rating from the database.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("DELETE FROM Ratings WHERE rating_id = ?", (rating_id,))
        conn.commit()
        conn.close()

    def list_ratings_per_course(self, course_id):
        """
        Returns all ratings given to a specific course.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT * FROM Ratings WHERE course_id = ?", (course_id,))
        results = c.fetchall()
        conn.close()
        return [RatingDTO(*row) for row in results]

    def list_ratings_per_student(self, student_id):
        """
        Returns all ratings made by a specific student.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT * FROM Ratings WHERE student_id = ?", (student_id,))
        results = c.fetchall()
        conn.close()
        return [RatingDTO(*row) for row in results]

    def average_rating_for_course(self, course_id):
        """
        Calculates the average rating for a specific course.
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Enabling foreign key constraint enforcement
        c = conn.cursor()
        c.execute("SELECT AVG(rating_value) FROM Ratings WHERE course_id = ?", (course_id,))
        avg = c.fetchone()[0]
        conn.close()
        return avg

# Example Usage
if __name__ == "__main__":
    dao = RatingDAO()
    
    # Create a new rating
    new_rating = RatingDTO(rating_id=1, course_id=1, student_id=1, rating_value=4)
    dao.create_rating(new_rating)

    # Read a rating's details
    rating = dao.read_rating(1)
    print(rating)

    # Update a rating's details
    updated_rating = RatingDTO(rating_id=1, course_id=1, student_id=1, rating_value=5)
    dao.update_rating(updated_rating)

    # Read the updated rating's details
    rating = dao.read_rating(1)
    print(f'updated: {rating}')

    # List all ratings for a course
    ratings_course = dao.list_ratings_per_course(1)
    print(f'courses ratings: {ratings_course}')

    # List all ratings for a student
    ratings_student = dao.list_ratings_per_student(1)
    print(f'student ratings: {ratings_student}')

    # Get average rating for a course
    avg_rating = dao.average_rating_for_course(1)
    print(f"Average Rating for Course 101: {avg_rating}")

    # Delete a rating
    dao.delete_rating(1)

    # Read a rating's details
    rating = dao.read_rating(1)
    print(rating)