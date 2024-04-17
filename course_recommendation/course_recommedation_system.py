import numpy as np
import pickle
import json
from models import KNNModel
from course_recommendation_form import CourseForm


class CourseRecommendationSystem:
    def __init__(self, model):
        self.course_features_aggregated = self.load_course_features()
        self.course_feedback_forms_by_student = self.load_course_feedback_forms()
        self.courses = self.load_courses()
        self.course_features_filtered = {}
        self.model = model

    def load_courses(self):
        with open('SE_Project/data_generation/courses.json') as file:
            courses_data = json.load(file)
        courses = {course['ID']: course for course in courses_data}
        return courses

    def load_course_features(self):
        with open('SE_Project/data_generation/course_features_aggregated.pkl', 'rb') as file:
            course_features_aggregated = pickle.load(file)
        return course_features_aggregated

    def load_course_feedback_forms(self):
        with open('SE_Project/data_generation/course_feedback_forms_by_student.json') as file:
            course_feedback_forms_by_student = json.load(file)
        return course_feedback_forms_by_student

    def get_courses_taken(self, roll_number):
        courses_taken = self.course_feedback_forms_by_student[roll_number]
        return courses_taken

    def get_course_features_taken(self, courses_taken, n):
        course_features_taken = {course: self.course_features_aggregated[course][:n+1] for course in courses_taken}
        return course_features_taken

    def get_student_profile_vector(self, course_features_taken,n):
        course_features_weighted = np.array([course_features_taken[course]*(course_features_taken[course][n]/10) for course in course_features_taken])
        course_features_weighted = np.array([course[:n] for course in course_features_weighted])
        student_profile_vector = np.mean(course_features_weighted, axis=0)
        return student_profile_vector

    def filter_courses(self, course_type):
        self.course_features_filtered = {course: self.course_features_aggregated[course] for course in self.course_features_aggregated if course[:2] == course_type}
        self.course_features_filtered = {course: self.course_features_filtered[course] for course in self.course_features_filtered if course[2:4] == '23'}

    def recommend_courses(self, user_preferences, feature_labels):
        indices = self.model.recommend(user_preferences)
        print('\nRecommended courses:\n')
        for index in indices:
            course_id = list(self.course_features_filtered.keys())[index]
            print(self.courses[course_id]['Name'])
            print('Course ID: ', course_id)
            for i in range(8):
                print(feature_labels[i], ': ', self.course_features_filtered[course_id][i])
            print('')

    def print_courses_taken_aggregated(self, courses_taken_aggregated,feature_labels):
        print('\nAggregated features of the courses you have taken:\n')
        for i in range(8):
            print(feature_labels[i], ': ', courses_taken_aggregated[i])
        print('')

    def print_similar_courses(self, courses_taken_aggregated,feature_labels):
        indices_similar = self.model.recommend(courses_taken_aggregated)
        print('\nCourses similar to the ones you have taken:\n')
        for index in indices_similar:
            course_id = list(self.course_features_filtered.keys())[index]
            print(self.courses[course_id]['Name'])
            print('Course ID: ', course_id)
            for i in range(8):
                print(feature_labels[i], ': ', self.course_features_filtered[course_id][i])
            print('')

    def run(self):
        form= CourseForm()
        roll_number, course_type, user_preferences, feature_labels = form.get_user_info()
        no_of_features = len(user_preferences)
        courses_taken = self.get_courses_taken(roll_number)
        course_features_taken = self.get_course_features_taken(courses_taken, no_of_features)
        student_profile_vector = self.get_student_profile_vector(course_features_taken, no_of_features)
        self.filter_courses(course_type)
        self.model.fit(np.array([self.course_features_filtered[course][:no_of_features] for course in self.course_features_filtered]))
        self.recommend_courses(user_preferences, feature_labels)
        self.print_courses_taken_aggregated(student_profile_vector,feature_labels)
        self.print_similar_courses(student_profile_vector,feature_labels)

if __name__ == '__main__':
    model = KNNModel(n_neighbors=3)
    recommendation_system = CourseRecommendationSystem(model)
    recommendation_system.run()











