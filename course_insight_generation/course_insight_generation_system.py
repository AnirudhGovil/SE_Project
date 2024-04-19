import numpy as np
import json
import pickle

class CourseInsightGenerationSystem():
    def __init__(self,model):
        self.course_features_aggregated = self.load_course_features()
        self.course_feedback_forms_by_course = self.load_course_feedback_forms()
        self.courses = self.load_courses()
        self.course_features_filtered = {}
        self.model = model

    def load_courses(self):
        with open('courses.json') as file:
            courses_data = json.load(file)
        courses = {course['ID']: course for course in courses_data}
        return courses

    def load_course_features(self):
        with open('course_features_aggregated.pkl', 'rb') as file:
            course_features_aggregated = pickle.load(file)
        return course_features_aggregated

    def load_course_feedback_forms(self):
        with open('course_feedback_forms_by_course.json') as file:
            course_feedback_forms_by_course = json.load(file)
        return course_feedback_forms_by_course
    
    def get_insights_as_professor(self,professor_id):
        if professor_id not in self.courses:
            return None
        course_id = self.courses[professor_id]
        if course_id not in self.course_features_aggregated:
            return None
        else:
            for i in len(self.course_feedback_forms_by_course[course_id]):
                print(self.course_feedback_forms_by_course[course_id][i])
        return self.course_feedback_forms_by_course[course_id]
    
    def get_insights_as_student(self,student_id):
        if student_id not in self.course_feedback_forms_by_course:
            return None
        return self.course_feedback_forms_by_course[student_id]


    
