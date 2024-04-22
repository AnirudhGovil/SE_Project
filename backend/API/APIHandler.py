from flask import Flask
from backend.API.studentAPI import app_student
from backend.API.instructorAPI import app_instructor
# from backend.API.feedbackAPI import app_feedback
from backend.API.courseAPI import courseAPI
from backend.API.courseStudentAPI import courseStudentAPI
from backend.API.courseRecommendationAPI import courseRecommendationAPI

app = Flask(__name__)
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app,supports_credentials=True)

app.register_blueprint(app_student, url_prefix='/')

app.register_blueprint(app_instructor, url_prefix='/')

# app.register_blueprint(app_feedback, url_prefix='/')

app.register_blueprint(courseAPI, url_prefix='/')

app.register_blueprint(courseStudentAPI, url_prefix='/')

app.register_blueprint(courseRecommendationAPI, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
