import requests

def create_course():
    url = 'http://localhost:8080/create/course'

    course_data = {
        'course_id': 2,
        'name': 'Introduction to Flask',
        'session': 'Spring 2024',
        'instructor_id': 1
    }

    # Send POST request with JSON data
    response = requests.post(url, json=course_data)

    # Check if request was successful
    if response.status_code == 201:
        print('Course created successfully!')
    else:
        print('Failed to create course.')


def get_course():
    url = 'http://localhost:8080/course/1'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        course = response.json()
        print('Course details:')
        print(course)
    else:
        print('Failed to get course.')


def update_course():
    url = 'http://localhost:8080/update/course'

    # changed name to Advanced Flask
    course_data = {
        'course_id': 1,
        'name': 'Advanced Flask',
        'session': 'Fall 2024',
        'instructor_id': 3
    }

    # Send PUT request with JSON data
    response = requests.put(url, json=course_data)

    # Check if request was successful
    if response.status_code == 200:
        print('Course updated successfully!')
    else:
        print('Failed to update course.')


def delete_course():
    url = 'http://localhost:8080/delete/course/2'

    # Send DELETE request
    response = requests.delete(url)

    # Check if request was successful
    if response.status_code == 200:
        result = response.json()
        success = result.get('success')
        if success:
            print('Course deleted successfully!')
        else:
            print('Failed to delete course.')
    else:
        print('Request failed with status code:', response.status_code)


def list_all_courses():
    url = 'http://localhost:8080/courses'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        courses = response.json()
        print('All courses:')
        print(courses)
    else:
        print('Failed to get all courses.')


def list_courses_by_instructor():
    url = 'http://localhost:8080/courses/instructor/3'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        courses = response.json()
        print('Courses taught by instructor:')
        print(courses)
    else:
        print('Failed to get courses.')


def list_courses_by_session():
    url = 'http://localhost:8080/courses/session/Monsoon2024'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        courses = response.json()
        print('Courses in session:')
        print(courses)
    else:
        print('Failed to get courses.')

def list_all_generatedCourses():
    url = 'http://localhost:8080/generatedCourses'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        courses = response.json()
        print('All generated courses:')
        print(courses)
    else:
        print('Failed to get all generated courses.')


if __name__ == '__main__':

    # 1. Test create_course()
    create_course()

    # # 2. Test get_course()
    get_course()

    # # 3. Test update_course()
    # update_course()

    # # 4. Test delete_course()
    # delete_course()

    # # 5. Test list_all_courses()
    list_all_courses()

    # # 6. Test list_courses_by_instructor()
    list_courses_by_instructor()

    # # 7. Test list_courses_by_session()
    list_courses_by_session()

    # # 8. Test list_all_generatedCourses()
    # list_all_generatedCourses()
