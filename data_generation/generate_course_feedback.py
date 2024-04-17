import numpy as np
import json

# Read the courses.json file

with open('courses.json') as f:
    courses = json.load(f)

# Create a courses dictionary with the course id as the key
courses = {course['ID']: course for course in courses}

# Create a list of course ids
course_ids = list(courses.keys())

# We shall generate a bunch of students

students_rolls = []

# Each student will have a unique id i.e. their roll number

# The roll number will be a string of the form YYYYXXXZZZ where YYYY is the year of joining, XXX is the department code and ZZZ is a unique number

# The department codes are as follows:
years = ['2017', '2018', '2019', '2020', '2021']
departments = ['101', '102', '103', '104']

# We will generate 1000 students

for i in range(1000):
    year = np.random.choice(years)
    department = np.random.choice(departments)
    # The unique number will be a random 3 digit number
    unique_number = np.random.randint(100, 1000)
    roll_number = year + department + str(unique_number)
    students_rolls.append(roll_number)

# Each student will take between 10 and 40 courses
students = {}
for student in students_rolls:
    num_courses = np.random.randint(10, 41)
    student_courses = np.random.choice(course_ids, num_courses, replace=False)
    students[student] = student_courses

# We will now generate feedback forms for each student
course_feedback_forms = {}
# Each feedback form will be indexed by the student's roll number + course id

for student in students:
    course_feedback_forms[student] = {}
    for course in students[student]:
        alpha = np.random.randint(1,11)
        beta = np.random.randint(1,11)
        gamma = np.random.randint(1,11)
        delta = np.random.randint(1,11)
        course_feedback_forms[student][course] = {
            'How would you rate the difficulty of the course?': alpha,
            'How would you rate the extent of time commitment required for the course?': int(((alpha + np.random.randint(-1, 2))/11)*10),
            'How well do you think the course was structured?': beta,
            'How would you rate the quality of the course material?': int(((beta + np.random.randint(-1, 2))/11)*9)+1,
            'How would you rate the quality of the assignments?': int(((beta + np.random.randint(-1, 2))/11)*9)+1,
            'How would you rate the quality of the exams?': int(((beta + np.random.randint(-1, 2))/11)*9)+1,
            'How well did the course align with your expectations?': gamma,
            'How likely are you to this course to your juniors?': int(((beta - alpha + gamma)/30)*9)+1,
            courses[course]['Questions'][0]: int(((delta + np.random.randint(-1, 2))/11)*9)+1,
            courses[course]['Questions'][1]: int(((delta + np.random.randint(-1, 2))/11)*9)+1,
            courses[course]['Questions'][2]: int(((delta + np.random.randint(-1, 2))/11)*9+1)
        }

# Reorganize the feedback forms by course
course_feedback_forms_by_course = {}
for student in course_feedback_forms:
    for course in course_feedback_forms[student]:
        if course not in course_feedback_forms_by_course:
            course_feedback_forms_by_course[course] = []
        course_feedback_forms_by_course[course].append({
            'Student': student,
            'Feedback': course_feedback_forms[student][course]
        })

# Save the feedback forms by course to a json file
with open('course_feedback_forms_by_course.json', 'w') as f:
    json.dump(course_feedback_forms_by_course, f, indent=4)


# Save the feedback forms to a json file
with open('course_feedback_forms_by_student.json', 'w') as f:
    json.dump(course_feedback_forms, f, indent=4)


# Create a students dictionary with the student roll number as the key
students_dict = {student: [] for student in students_rolls}
# Add the courses IDs and names each student has taken
for student in students:
    for course in students[student]:
        students_dict[student].append({
            'Course ID': course,
            'Course Name': courses[course]['Name'],
            'Feedback': course_feedback_forms[student][course]
        })

# Save the students dictionary to a json file
with open('students.json', 'w') as f:
    json.dump(students_dict, f, indent=4)