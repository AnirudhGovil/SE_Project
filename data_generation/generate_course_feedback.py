import numpy as np
import json
import random


# Read the courses.json file

with open('courses.json') as file:
    courses_data = json.load(file)

with open('feedback_questions.json') as file:
    feedback_questions = json.load(file)

print(feedback_questions)


# Create a courses dictionary with the course id as the key
courses = {course['ID']: course for course in courses_data}

# Create a list of course ids
course_ids = list(courses.keys())

# We shall generate a bunch of students

student_roll_numbers = []

# Each student will have a unique id i.e. their roll number

# The roll number will be a string of the form YYYYXXXZZZ where YYYY is the year of joining, XXX is the department code and ZZZ is a unique number

# The department codes are as follows:
joining_years = ['2018', '2019', '2020', '2021']
department_codes = ['101', '102', '103', '104']
# We will generate 1000 students

for i in range(1000):
    year = np.random.choice(joining_years)
    department = np.random.choice(department_codes)
    # The unique number will be a random 3 digit number
    unique_number = np.random.randint(100, 1000)
    roll_number = year + department + str(unique_number)
    student_roll_numbers.append(roll_number)


# We will now assign a professor to each course, for each course check if the Category matches the professor's Category
for course in courses:
    category = courses[course]['Category']
    courses[course]['Professor'] = category + str(np.random.randint(10, 100))

# Now we can get a list of professors
professors = list(set([courses[course]['Professor'] for course in courses]))

# We can even create a dictionary of professors with the professor id as the key
professors_dict = {professor: [] for professor in professors}

# Add the courses each professor is teaching
for course in courses:
    professors_dict[courses[course]['Professor']].append({
        'Course ID': course,
        'Course Name': courses[course]['Name']
    })

# Save the professors dictionary to a json file
with open('professors.json', 'w') as file:
    json.dump(professors_dict, file, indent=4)


# Now we will generate a profile vector for each course with 12 features
course_profile_vectors = {}
for course in courses:
    # Create a vector with 13 random number between 1 and 10
    course_profile_vectors[course] = np.random.randint(1, 11, 12)

    
# Each student will take between 10 and 40 courses
students = {}
for student_roll_number in student_roll_numbers:
    num_courses = np.random.randint(5, 30)
    student_courses = np.random.choice(course_ids, num_courses, replace=False)
    students[student_roll_number] = student_courses

# Ensure that no student has taken the same course twice
for student in students:
    students[student] = list(set(students[student]))  

# Ensure that no student has taken both the 22 and 23 versions of the same course
for student in students:
    for course in students[student]:
        if course[-2:] == '22':
            if course[:-2]+'23' in students[student]:
                students[student].remove(course[:-2]+'23')
        if course[-2:] == '23':
            if course[:-2]+'22' in students[student]:
                students[student].remove(course[:-2]+'22')        

# We will now generate feedback forms for each student
course_feedback_forms = {}
# Each feedback form will be indexed by the student's roll number + course id

for student in students:
    course_feedback_forms[student] = {}
    # Create a vector with 12 random number between 2 and 9
    student_profile_vector = np.random.randint(1, 11, 12)
    for course in students[student]:
        # Generate a noise vector with 12 random integers between 1 and 10
        noise_vector = np.random.randint(1, 11, 12)
        # Combine the student profile vector and the noise vector
        student_profile_vector = np.mean([student_profile_vector, noise_vector], axis=0)
        # Offset the course profile vector
        student_profile_vector = np.mean([student_profile_vector, course_profile_vectors[course]], axis=0)
        # Now the values lie between 1 and 10, convert all values to ints
        student_profile_vector = [int(np.round(value)) for value in student_profile_vector]

        course_feedback_forms[student][course] = {
            feedback_questions[0]: student_profile_vector[0],
            feedback_questions[1]: student_profile_vector[1],
            feedback_questions[2]: student_profile_vector[2],
            feedback_questions[3]: student_profile_vector[3],
            feedback_questions[4]: student_profile_vector[4],
            feedback_questions[5]: student_profile_vector[5],
            feedback_questions[6]: student_profile_vector[6],
            feedback_questions[7]: student_profile_vector[7],
            courses[course]['Questions'][0]: student_profile_vector[8],
            courses[course]['Questions'][1]: student_profile_vector[9],
            courses[course]['Questions'][2]: student_profile_vector[10],
            feedback_questions[8]: student_profile_vector[11],
            feedback_questions[9]: int((np.sum(student_profile_vector[2:8]) - np.sum(student_profile_vector[0:2]) + np.random.randint(-10, 11) + 30) // 10 + 1)
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
with open('course_feedback_forms_by_course.json', 'w') as file:
    json.dump(course_feedback_forms_by_course, file, indent=4)


# Save the feedback forms to a json file
with open('course_feedback_forms_by_student.json', 'w') as file:
    json.dump(course_feedback_forms, file, indent=4)


# Create a students dictionary with the student roll number as the key
students_dict = {student: [] for student in student_roll_numbers}
# Add the courses IDs and names each student has taken
for student in students:
    for course in students[student]:
        students_dict[student].append({
            'Course ID': course,
            'Course Name': courses[course]['Name'],
            'Feedback': course_feedback_forms[student][course]
        })

# Save the students dictionary to a json file
with open('students.json', 'w') as file:
    json.dump(students_dict, file, indent=4)

    
