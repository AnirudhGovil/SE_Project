from flask import Flask, request, jsonify
from flask import Blueprint
from backend.DAO.instructorDAO import InstructorDAO
from backend.DTO.instructorDTO import InstructorDTO

app_instructor = Blueprint('instructorAPI', __name__)


@app_instructor.route('/sign_up/instructor', methods=['POST'])
def sign_up():
    '''
    param: instructor_dto
    output: create instructor in the database and return bool success
    '''
    data = request.get_json()
    instructor_dto = InstructorDTO(data['instructor_id'], data['name'], data['email'])
    instructor_dao = InstructorDAO()
    success = instructor_dao.create_instructor(instructor_dto)
    return jsonify({'success': success})


@app_instructor.route('/login/instructor', methods=['GET'])
def login():
    """
    param: instructor_id
    output: instructor_dto or None.
    """
    data = request.get_json()
    instructor_id = data['instructor_id']
    instructor_dao = InstructorDAO()
    instructor_dto = instructor_dao.read_instructor(instructor_id)
    return jsonify({'instructor': instructor_dto})


@app_instructor.route('/update/instructor', methods=['POST'])
def update_instructor():
    """
    param: instructor_dto
    output: bool success
    """
    data = request.get_json()
    instructor_dto = InstructorDTO(data['instructor_id'], data['name'], data['email'])
    instructor_dao = InstructorDAO()
    success = instructor_dao.update_instructor(instructor_dto)
    return jsonify({'success': success})


@app_instructor.route('/delete/instructor', methods=['GET'])
def delete_instructor():
    """
    param: instructor_id (attached in the URL)
    output: bool success
    """
    data = request.get_json()
    instructor_id = data['instructor_id']
    instructor_dao = InstructorDAO()
    success = instructor_dao.delete_instructor(instructor_id)
    return jsonify({'success': success})