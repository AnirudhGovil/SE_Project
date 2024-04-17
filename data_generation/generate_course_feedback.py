import numpy as np
import json

# Read the courses.json file

with open('courses.json') as file:
    courses_data = json.load(file)

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
    for course in students[student]:
        difficulty_rating = np.random.randint(1,11)
        time_commitment_rating = np.random.randint(1,11)
        learning_rating = np.random.randint(1,11)
        course_structure_rating = np.random.randint(1,11)
        material_quality_rating = np.random.randint(1,11)
        assignment_quality_rating = np.random.randint(1,11)
        exam_quality_rating = np.random.randint(1,11)
        expectation_alignment_rating = np.random.randint(1,11)
        recommendation_likelihood_rating = np.random.randint(1,11)
        course_specific_question1_rating = np.random.randint(1,11)
        course_specific_question2_rating = np.random.randint(1,11)
        course_specific_question3_rating = np.random.randint(1,11)
        instructor_quality_rating = np.random.randint(1,11)
        course_feedback_forms[student][course] = {
            'How would you rate the difficulty of the course?': difficulty_rating,
            'How would you rate the extent of time commitment required for the course?': int(((difficulty_rating + np.random.randint(-1, 2))/11)*9)+1,
            'How much would you say you learned from the course?': learning_rating,
            'How well do you think the course was structured?': course_structure_rating,
            'How would you rate the quality of the course material?': int(((course_structure_rating + np.random.randint(-1, 2))/11)*9)+1,
            'How would you rate the quality of the assignments?': int(((course_structure_rating + np.random.randint(-1, 2))/11)*9)+1,
            'How would you rate the quality of the exams?': int(((course_structure_rating + np.random.randint(-1, 2))/11)*9)+1,
            'How well did the course align with your expectations?': expectation_alignment_rating,
            'How likely are you to recommend this course to your juniors?': int(((course_structure_rating - difficulty_rating + expectation_alignment_rating + learning_rating + instructor_quality_rating)/50)*9)+1,
            courses[course]['Questions'][0]: int(((recommendation_likelihood_rating + np.random.randint(-1, 2))/11)*9)+1,
            courses[course]['Questions'][1]: int(((recommendation_likelihood_rating + np.random.randint(-1, 2))/11)*9)+1,
            courses[course]['Questions'][2]: int(((recommendation_likelihood_rating + np.random.randint(-1, 2))/11)*9+1),
            'How would you rate the quality of your instructor?': instructor_quality_rating
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

# Since we used random numbers to generate the feedback forms, all courses once aggregated will have similar features
# To force the courses to have different features, we will add a random number to the features of each course

for course in course_feedback_forms_by_course:
    difficulty_rating = np.random.randint(1,11)
    course_structure_rating = np.random.randint(1,11)
    expectation_alignment_rating = np.random.randint(1,11)
    recommendation_likelihood_rating = np.random.randint(1,11)
    instructor_quality_rating = np.random.randint(1,11)
    offset = [difficulty_rating, difficulty_rating, learning_rating, course_structure_rating, course_structure_rating, course_structure_rating, course_structure_rating, expectation_alignment_rating, course_structure_rating - difficulty_rating + expectation_alignment_rating + learning_rating, course_specific_question1_rating, course_specific_question2_rating, course_specific_question3_rating, instructor_quality_rating]
    for feedback in course_feedback_forms_by_course[course]:
        i = 0
        for key in feedback['Feedback']:
            feedback['Feedback'][key] += offset[i]
            i += 1
            # Normalize the feedback to be between 1 and 10 by dividing by 12 and multiplying by 10
            feedback['Feedback'][key] = int((feedback['Feedback'][key]/20)*9)+1

# Make sure the changes are reflected in the course_feedback_forms dictionary
for course in course_feedback_forms_by_course:
    for feedback in course_feedback_forms_by_course[course]:
        course_feedback_forms[feedback['Student']][course] = feedback['Feedback']


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

    
