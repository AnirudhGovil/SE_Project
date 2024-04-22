import sqlite3
import os

# Function to delete "Courses.db", if it exists

def delete_database():
    try:
        os.remove('Course.db')
    except FileNotFoundError:
        pass

def create_database():
    # Connecting to SQLite3 memory-based database
    conn = sqlite3.connect('Course.db')
    c = conn.cursor()

    # Creating the tables based on the provided schema

    # Instructors Table
    c.execute('''
        CREATE TABLE Instructors (
            instructor_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE
        )
    ''')

    # Students Table
    c.execute('''
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            roll_number INTEGER UNIQUE
        )
    ''')

    # Creating the Courses Table 
    c.execute('''
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            name TEXT,
            session TEXT,
            instructor_id INTEGER,
            FOREIGN KEY(instructor_id) REFERENCES Instructors(instructor_id)
        )
    ''')

    # Creating a many-to-many relationship table for students and courses
    c.execute('''
        CREATE TABLE CourseStudents (
            course_id INTEGER,
            student_id INTEGER,
            PRIMARY KEY (course_id, student_id),
            FOREIGN KEY(course_id) REFERENCES Courses(course_id),
            FOREIGN KEY(student_id) REFERENCES Students(student_id)
        )
    ''')

    # Ratings Table
    c.execute('''
        CREATE TABLE Ratings (
            rating_id INTEGER PRIMARY KEY,
            course_id INTEGER,
            student_id INTEGER,
            rating_value INTEGER,
            FOREIGN KEY(course_id) REFERENCES Courses(course_id),
            FOREIGN KEY(student_id) REFERENCES Students(student_id)
        )
    ''')

    # Feedback Table
    c.execute('''
        CREATE TABLE Feedback (
            feedback_id INTEGER PRIMARY KEY,
            course_id INTEGER,
            student_id INTEGER,
            feedback_text TEXT,
            FOREIGN KEY(course_id) REFERENCES Courses(course_id),
            FOREIGN KEY(student_id) REFERENCES Students(student_id)
        )
    ''')

    conn.commit()
    conn.close()


def view_database():
    # Connect to SQLite database
    conn = sqlite3.connect('Course.db')
    cursor = conn.cursor()

    # Execute a SELECT Courses to retrieve all rows from the events table
    cursor.execute('SELECT * FROM Courses')

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close connection
    conn.close()


def main():
    delete_database()
    create_database()
    view_database()


if __name__ == "__main__":
    main()