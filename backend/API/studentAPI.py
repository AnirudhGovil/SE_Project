from flask import Flask, request, jsonify
from flask import Blueprint
from backend.DAO.studentDAO import StudentDAO
from backend.DTO.studentDTO import StudentDTO

app_student = Blueprint('studentAPI', __name__)


@app_student.route('/sign_up/student', methods=['POST'])
def sign_up():
    '''
    param: student_dto
    output: create student in the database and return bool success
    '''
    data = request.get_json()
    student_dto = StudentDTO(data['student_id'], data['name'], data['email'], data['roll_number'])
    student_dao = StudentDAO()
    success = student_dao.create_student(student_dto)
    return jsonify({'success': success})


@app_student.route('/login/student', methods=['GET'])
def login():
    """
    param: student_id
    output: student_dto or None.
    """
    data = request.get_json()
    student_id = data['student_id']
    student_dao = StudentDAO()
    student_dto = student_dao.read_student(student_id)
    return jsonify({'student': student_dto})


@app_student.route('/update/student', methods=['POST'])
def update_student():
    """
    param: student_dto
    output: bool success
    """
    data = request.get_json()
    student_dto = StudentDTO(data['student_id'], data['name'], data['email'], data['roll_number'])
    student_dao = StudentDAO()
    success = student_dao.update_student(student_dto)
    return jsonify({'success': success})


@app_student.route('/delete/student', methods=['GET'])
def delete_student():
    """
    param: student_id (attached in the URL)
    output: bool success
    """
    data = request.get_json()
    student_id = data['student_id']
    student_dao = StudentDAO()
    success = student_dao.delete_student(student_id)
    return jsonify({'success': success})