from models.models import KNNModel
from course_recommendation.course_recommendation_form import CourseRecommedationForm
from course_recommendation.course_recommedation_system import CourseRecommendationSystem

import numpy as np

def main():
        """
        Runs the course recommendation system.
        """
        model = KNNModel(n_neighbors=3)
        form = CourseRecommedationForm()
        system = CourseRecommendationSystem(model)
        roll_number, course_type, user_preferences, feature_labels, feature_keys = form.get_user_info()
        no_of_features = len(user_preferences)
        student_profile_vector= system.get_student_profile_vector(roll_number, feature_keys, feature_labels)
        system.filter_courses(course_type)
        system.model.fit(np.array([system.course_features_filtered[course][:no_of_features] for course in system.course_features_filtered]))
        system.recommend_courses(user_preferences, feature_labels)
        system.print_similar_courses(student_profile_vector, feature_labels)

if __name__ == '__main__':
    main()