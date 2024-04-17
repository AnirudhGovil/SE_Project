import json
import numpy as np
import pickle

# Read the SE_Project/data_generation/course_feedback_forms_by_course.json and SE_Project/data_generation/course_feedback_forms_by_student.json files

with open('course_feedback_forms_by_course.json') as f:
    course_feedback_forms_by_course = json.load(f)

# Create a dictionary of course feedback forms indexed by course id
course_feedback_forms = {}
for course in course_feedback_forms_by_course:
    course_feedback_forms[course] = {}
    for feedback in course_feedback_forms_by_course[course]:
        course_feedback_forms[course][feedback['Student']] = feedback['Feedback']


# Now create vector of features for each course
course_features = {}
for course in course_feedback_forms:
    course_features[course] = np.array([list(feedback.values()) for feedback in course_feedback_forms[course].values()])

# Aggregate the features for each course
course_features_aggregated = {}
for course in course_features:
    course_features_aggregated[course] = np.mean(course_features[course], axis=0)

# Save the aggregated features to a pkl file
with open('course_features_aggregated.pkl', 'wb') as f:
    pickle.dump(course_features_aggregated, f)

# Read the professors.json file
with open('professors.json') as f:
    professors = json.load(f)

# For each professor, assign them the course_features_aggregated of the courses they are teaching
professor_features = {}
for professor in professors:
    professor_features[professor] = []
    for course in professors[professor]:
        professor_features[professor].append(course_features_aggregated[course['Course ID']])

# Save the professor features to a pkl file
with open('professor_features.pkl', 'wb') as f:
    pickle.dump(professor_features, f)

# Now to create student features, we must find out which courses each student has taken, and what feedback they have given
with open('course_feedback_forms_by_student.json') as f:
    course_feedback_forms_by_student = json.load(f)

student_features = {}
for student in course_feedback_forms_by_student:
    student_dict = {}
    for feedback in course_feedback_forms_by_student[student]:
        student_dict[feedback] = np.array(list(course_feedback_forms_by_student[student][feedback].values()))
    student_features[student] = student_dict

# Dump the student features to a pkl file
with open('student_features.pkl', 'wb') as f:
    pickle.dump(student_features, f)






