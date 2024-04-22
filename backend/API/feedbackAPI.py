from flask import Flask, request, jsonify
from flask import Blueprint
from backend.DAO.feedbackDAO import FeedbackDAO
from backend.DTO.feedbackDTO import FeedbackDTO

feedback_dao = FeedbackDAO()

app_instructor = Blueprint('feedbackAPI', __name__)

@app_instructor.route('/feedback/create', methods=['POST'])
def create_feedback():
    """
    Endpoint to create a new feedback.
    """
    data = request.get_json()
    feedback_dto = FeedbackDTO(**data)
    feedback_dao = FeedbackDAO()
    feedback_dao.create_feedback(feedback_dto)
    return jsonify({'message': 'Feedback created successfully'}), 201

@app_instructor.route('/feedback/<int:feedback_id>', methods=['GET'])
def get_feedback(feedback_id):
    """
    Endpoint to get details of a feedback by feedback ID.
    """
    feedback_dao = FeedbackDAO()
    feedback = feedback_dao.read_feedback(feedback_id)
    if feedback:
        return jsonify(feedback.__dict__)
    else:
        return jsonify({'message': 'Feedback not found'}), 404

@app_instructor.route('/feedback/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    """
    Endpoint to update a feedback by feedback ID.
    """
    data = request.get_json()
    data['feedback_id'] = feedback_id
    updated_feedback = FeedbackDTO(**data)
    feedback_dao = FeedbackDAO()
    feedback_dao.update_feedback(updated_feedback)
    return jsonify({'message': 'Feedback updated successfully'})

@app_instructor.route('/feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """
    Endpoint to delete a feedback by feedback ID.
    """
    feedback_dao = FeedbackDAO()
    feedback_dao.delete_feedback(feedback_id)
    return jsonify({'message': 'Feedback deleted successfully'})

@app_instructor.route('/feedback/course/<int:course_id>', methods=['GET'])
def list_feedback_by_course(course_id):
    """
    Endpoint to list all feedbacks for a specific course.
    """
    feedback_dao = FeedbackDAO()
    feedbacks = feedback_dao.list_feedback_by_course(course_id)
    return jsonify([feedback.__dict__ for feedback in feedbacks])

@app_instructor.route('/feedback/student/<int:student_id>', methods=['GET'])
def list_feedback_by_student(student_id):
    """
    Endpoint to list all feedbacks made by a specific student.
    """
    feedback_dao = FeedbackDAO()
    feedbacks = feedback_dao.list_feedback_by_student(student_id)
    return jsonify([feedback.__dict__ for feedback in feedbacks])

