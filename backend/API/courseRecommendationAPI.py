from flask import Flask, request, jsonify, Blueprint
from models.models import KNNModel
from course_recommendation.course_recommedation_system import CourseRecommendationSystem
import numpy as np

courseRecommendationAPI = Blueprint('courseRecommendationAPI', __name__)

@courseRecommendationAPI.route('/recommend_courses', methods=['POST'])
def recommend_courses():
    """
    Endpoint to receive user preferences and recommend courses.
    """
    data = request.get_json()
    roll_number = data['roll_number']
    course_type = data['course_type']
    user_preferences = np.array(data['user_preferences'])
    feature_labels = data['feature_labels']
    feature_keys = data['feature_keys']

    model = KNNModel(n_neighbors=3)
    system = CourseRecommendationSystem(model)

    no_of_features = len(user_preferences)
    student_profile_vector = system.get_student_profile_vector(roll_number, feature_keys, feature_labels)
    system.filter_courses(course_type)
    system.model.fit(np.array([system.course_features_filtered[course][:no_of_features] for course in system.course_features_filtered]))

    recommended_courses= system.recommend_courses(user_preferences, feature_labels)
    similar_courses= system.print_similar_courses(student_profile_vector, feature_labels)

    return jsonify({
        'student_profile_vector': student_profile_vector.tolist(),
        'recommended_courses': recommended_courses,
        'similar_courses': similar_courses
    })
