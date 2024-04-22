import numpy as np
import json

class CourseRecommedationForm:
    """
    A class to represent a course recommendation form.

    Methods:
    - get_user_info: Gets the user's course preferences.
    """

    def __init__(self):
        # Read the keys from the json file
        with open('data_generation/feedback_questions.json') as file:
            feedback_questions = json.load(file)
        self.feature_keys = feedback_questions
        self.feature_labels = ['Difficulty', 'Time commitment', 'New learning', 'Structure quality', 'Material quality', 'Assignment quality', 'Exam quality', 'Expectation alignment', 'Instructor quality', 'Recommendation Likelihood']
        self.categories =  ['SC', 'MA', 'EE', 'HU', 'CS']

    def get_user_info(self):
        """
        Gets the user's course preferences.

        Returns:
        - roll_number: The roll number of the student.
        - course_type: The type of course the student is looking for.
        - user_preferences: The user's preferences for course features.
        - feature_labels: The labels of the course features.
        """
        
        course_type = int(input('What type of course are you looking for?\n [1 : Science, 2 : Mathematics, 3 : Electrical Engineering, 4 : Humanities, 5 : Computer Science]: '))
        course_type = self.categories[course_type-1]
        roll_number = input('Enter your roll number: ')
        difficulty = int(input('What difficulty are you willing to tolerate? (1-10): '))
        time_commitment = int(input('How much time can you commit to the course? (1-10): '))
        new_learning = int(input('How important is it to you to learn something new from the course? (1-10): '))
        structure_quality = int(input('How important is it to you that the course is well structured? (1-10): '))
        material_quality = int(input('How much do you value the quality of the course material? (1-10): '))
        assignment_quality = int(input('How much do you value the quality of the assignments? (1-10): '))
        exam_quality = int(input('How much do you value the quality of the exams? (1-10): '))
        expectation_alignment = int(input('How important is it to you that the course aligns with your expectations? (1-10): '))
        instructor_quality = int(input('How much do you value the quality of the instructor? (1-10): '))
        recommendation_likelihood = int(input('How important are other students\' recommendations to you? (1-10): '))
        user_preferences = np.array([-(1/difficulty), time_commitment, new_learning, structure_quality, material_quality, assignment_quality, exam_quality, expectation_alignment, instructor_quality, recommendation_likelihood])
        return roll_number, course_type, user_preferences, self.feature_labels, self.feature_keys