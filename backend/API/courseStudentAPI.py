from flask import Flask, request, jsonify, Blueprint
from backend.DAO.courseStudentDAO import CourseStudentDAO
from backend.DTO.courseStudentDTO import CourseStudentDTO

courseStudentAPI = Blueprint('courseStudentAPI', __name__)

@courseStudentAPI.route('/create/course_student', methods=['POST'])
def create_course_student():
    """
    Endpoint to create a new course-student relationship.
    """
    data = request.get_json()
    course_student_dto = CourseStudentDTO(**data)
    course_student_dao = CourseStudentDAO()
    success = course_student_dao.create_course_student(course_student_dto)
    return jsonify({'success': success}), 201

@courseStudentAPI.route('/course_student/<int:course_id>/<int:student_id>', methods=['GET'])
def get_course_student(course_id, student_id):
    """
    Endpoint to get details of a course-student relationship by course ID and student ID.
    """
    course_student_dao = CourseStudentDAO()
    course_student = course_student_dao.read_course_student(course_id, student_id)
    if course_student:
        return jsonify(course_student.__dict__)
    else:
        return jsonify({'message': 'Course-student relationship not found'}), 404

@courseStudentAPI.route('/update/course_student', methods=['PUT'])
def update_course_student():
    """
    Endpoint to update a course-student relationship.
    """
    data = request.get_json()
    original_course_id = data.get('original_course_id')
    original_student_id = data.get('original_student_id')
    new_course_id = data.get('new_course_id')
    new_student_id = data.get('new_student_id')
    course_student_dao = CourseStudentDAO()
    success = course_student_dao.update_course_student(original_course_id, original_student_id, new_course_id, new_student_id)
    return jsonify({'success': success})

@courseStudentAPI.route('/delete/course_student/<int:course_id>/<int:student_id>', methods=['DELETE'])
def delete_course_student(course_id, student_id):
    """
    Endpoint to delete a course-student relationship by course ID and student ID.
    """
    course_student_dao = CourseStudentDAO()
    success = course_student_dao.delete_course_student(course_id, student_id)
    return jsonify({'success': success})

@courseStudentAPI.route('/courses/student/<int:student_id>', methods=['GET'])
def list_courses_by_student(student_id):
    """
    Endpoint to list all courses taken by a specific student.
    """
    course_student_dao = CourseStudentDAO()
    courses = course_student_dao.find_courses_by_student(student_id)
    return jsonify(courses)

@courseStudentAPI.route('/students/course/<int:course_id>', methods=['GET'])
def list_students_by_course(course_id):
    """
    Endpoint to list all students in a specific course.
    """
    course_student_dao = CourseStudentDAO()
    students = course_student_dao.find_students_by_course(course_id)
    return jsonify(students)
