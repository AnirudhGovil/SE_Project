from flask import Flask, request, jsonify, Blueprint
import json
from backend.DAO.courseDAO import CourseDAO
from backend.DTO.courseDTO import CourseDTO

courseAPI = Blueprint('courseAPI', __name__)

@courseAPI.route('/create/course', methods=['POST'])
def create_course():
    """
    Endpoint to create a new course.
    """
    data = request.get_json()
    course_dto = CourseDTO(**data)
    course_dao = CourseDAO()
    success = course_dao.create_course(course_dto)
    return jsonify({'success': success}), 201

@courseAPI.route('/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Endpoint to get details of a course by course ID.
    """
    course_dao = CourseDAO()
    course = course_dao.read_course(course_id)
    if course:
        return jsonify(course.__dict__)
    else:
        return jsonify({'message': 'Course not found'}), 404

@courseAPI.route('/update/course', methods=['PUT'])
def update_course():
    """
    Endpoint to update a course by course ID.
    """
    data = request.get_json()
    course_dto = CourseDTO(**data)
    course_dao = CourseDAO()
    success = course_dao.update_course(course_dto)
    return jsonify({'success': success})

@courseAPI.route('/delete/course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Endpoint to delete a course by course ID.
    """
    course_dao = CourseDAO()
    success = course_dao.delete_course(course_id)
    return jsonify({'success': success})

@courseAPI.route('/courses', methods=['GET'])
def list_all_courses():
    """
    Endpoint to list all courses.
    """
    course_dao = CourseDAO()
    courses = course_dao.list_all_courses()
    return jsonify([course.__dict__ for course in courses])

@courseAPI.route('/courses/instructor/<int:instructor_id>', methods=['GET'])
def list_courses_by_instructor(instructor_id):
    """
    Endpoint to list all courses taught by a specific instructor.
    """
    course_dao = CourseDAO()
    courses = course_dao.find_courses_by_instructor(instructor_id)
    return jsonify([course.__dict__ for course in courses])

@courseAPI.route('/courses/session/<session>', methods=['GET'])
def list_courses_by_session(session):
    """
    Endpoint to list all courses in a specific session.
    """
    course_dao = CourseDAO()
    courses = course_dao.find_courses_by_session(session)
    return jsonify([course.__dict__ for course in courses])

@courseAPI.route('/generatedCourses', methods=['GET'])
def list_all_generatedCourses():
    # Load data from the JSON file
    with open('data_generation/courses.json') as file:
        courses = json.load(file)
    return jsonify(courses)