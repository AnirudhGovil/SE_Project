import requests

def create_course_student():
    url = 'http://localhost:8080/create/course_student'

    course_student_data = {
        'course_id': 2,
        'student_id': 3
    }

    # Send POST request with JSON data
    response = requests.post(url, json=course_student_data)

    # Check if request was successful
    if response.status_code == 201:
        print('Course student relationship created successfully!')
    else:
        print('Failed to create course student relationship.')


def get_course_student():
    url = 'http://localhost:8080/course_student/2/1'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        course_student = response.json()
        print('Course student relationship details:')
        print(course_student)
    else:
        print('Failed to get course student relationship.')


def update_course_student():
    url = 'http://localhost:8080/update/course_student'

    # Update the course student relationship
    updated_course_student_data = {
        'original_course_id': 2,
        'original_student_id': 4,
        'new_course_id': 1,
        'new_student_id': 4
    }

    # Send PUT request with JSON data
    response = requests.put(url, json=updated_course_student_data)

    # Check if request was successful
    if response.status_code == 200:
        print('Course student relationship updated successfully!')
    else:
        print('Failed to update course student relationship.')


def delete_course_student():
    url = 'http://localhost:8080/delete/course_student/4/4'

    # Send DELETE request
    response = requests.delete(url)

    # Check if request was successful
    if response.status_code == 200:
        result = response.json()
        success = result.get('success')
        if success:
            print('Course student relationship deleted successfully!')
        else:
            print('Failed to delete course student relationship.')
    else:
        print('Request failed with status code:', response.status_code)


def list_courses_by_student():
    url = 'http://localhost:8080/courses/student/3'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        courses = response.json()
        print('Courses taken by student:')
        print(courses)
    else:
        print('Failed to get courses taken by student.')


def list_students_by_course():
    url = 'http://localhost:8080/students/course/2'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        students = response.json()
        print('Students in the course:')
        print(students)
    else:
        print('Failed to get students in the course.')


if __name__ == '__main__':
    # 1. Test create_course_student()
    create_course_student()

    # 2. Test get_course_student()
    get_course_student()

    # 3. Test update_course_student()
    # update_course_student()

    # 4. Test delete_course_student()
    # delete_course_student()

    # 5. Test list_courses_by_student()
    # list_courses_by_student()

    # 6. Test list_students_by_course()
    # list_students_by_course()
