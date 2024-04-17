import numpy as np
import pickle
import json

class CourseRecommendationSystem:
    def __init__(self, model):
        """
        Initializes the CourseRecommendationSystem object.

        Parameters:
        - model: The machine learning model used for course recommendation.
        """
        self.course_features_aggregated = self.load_course_features()
        self.course_feedback_forms_by_student = self.load_course_feedback_forms()
        self.courses = self.load_courses()
        self.course_features_filtered = {}
        self.model = model

    def load_courses(self):
        """
        Loads the course data from a JSON file.

        Returns:
        - courses: A dictionary containing course data, with course IDs as keys.
        """
        with open('data_generation/courses.json') as file:
            courses_data = json.load(file)
        courses = {course['ID']: course for course in courses_data}
        return courses

    def load_course_features(self):
        """
        Loads the aggregated course features from a pickle file.

        Returns:
        - course_features_aggregated: A dictionary containing aggregated course features, with course IDs as keys.
        """
        with open('data_generation/course_features_aggregated.pkl', 'rb') as file:
            course_features_aggregated = pickle.load(file)
        return course_features_aggregated

    def load_course_feedback_forms(self):
        """
        Loads the course feedback forms data from a JSON file.

        Returns:
        - course_feedback_forms_by_student: A dictionary containing course feedback forms data, with student roll numbers as keys.
        """
        with open('data_generation/course_feedback_forms_by_student.json') as file:
            course_feedback_forms_by_student = json.load(file)
        return course_feedback_forms_by_student

    def get_features_of_courses_taken(self, roll_number, n):
        """
        Retrieves the features of courses taken by a student.

        Parameters:
        - roll_number: The roll number of the student.
        - n: The number of features to retrieve.

        Returns:
        - features_of_courses_taken: A dictionary containing the features of courses taken by the student, with course IDs as keys.
        """
        courses_taken = self.course_feedback_forms_by_student[roll_number]
        features_of_courses_taken = {course: self.course_features_aggregated[course][:n+1] for course in courses_taken}
        return features_of_courses_taken
        
    def get_student_profile_vector(self, course_features_taken, n, feature_labels):
        """
        Calculates the student profile vector based on the features of courses taken.

        Parameters:
        - course_features_taken: A dictionary containing the features of courses taken by the student, with course IDs as keys.
        - n: The number of features to consider.
        - feature_labels: The labels of the features.

        Returns:
        - student_profile_vector: The student profile vector.
        """
        course_features_weighted = np.array([course_features_taken[course]*(course_features_taken[course][n]/10) for course in course_features_taken])
        course_features_weighted = np.array([course[:n] for course in course_features_weighted])
        student_profile_vector = np.mean(course_features_weighted, axis=0)

        print('\nAggregated features of the courses you have taken:\n')
        for i in range(8):
            print(feature_labels[i], ': ', student_profile_vector[i])
        print('')

        return student_profile_vector

    def filter_courses(self, course_type):
        """
        Filters the course features based on the course type.

        Parameters:
        - course_type: The type of courses to filter.

        Modifies:
        - self.course_features_filtered: Updates the filtered course features dictionary.
        """
        self.course_features_filtered = {course: self.course_features_aggregated[course] for course in self.course_features_aggregated if course[:2] == course_type}
        self.course_features_filtered = {course: self.course_features_filtered[course] for course in self.course_features_filtered if course[2:4] == '23'}

    def recommend_courses(self, user_preferences, feature_labels):
        """
        Recommends courses based on user preferences.

        Parameters:
        - user_preferences: The user's preferences for each feature.
        - feature_labels: The labels of the features.

        Prints:
        - Recommended courses with their details.
        """
        indices = self.model.recommend(user_preferences)
        print('\nRecommended courses:\n')
        for index in indices:
            course_id = list(self.course_features_filtered.keys())[index]
            print(self.courses[course_id]['Name'])
            print('Course ID: ', course_id)
            for i in range(8):
                print(feature_labels[i], ': ', self.course_features_filtered[course_id][i])
            print('')
        
    def print_similar_courses(self, courses_taken_aggregated, feature_labels):
        """
        Prints courses similar to the ones taken by the student.

        Parameters:
        - courses_taken_aggregated: The aggregated features of the courses taken.
        - feature_labels: The labels of the features.
        """
        indices_similar = self.model.recommend(courses_taken_aggregated)
        print('\nCourses similar to the ones you have taken:\n')
        for index in indices_similar:
            course_id = list(self.course_features_filtered.keys())[index]
            print(self.courses[course_id]['Name'])
            print('Course ID: ', course_id)
            for i in range(8):
                print(feature_labels[i], ': ', self.course_features_filtered[course_id][i])
            print('')

    











