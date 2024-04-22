import requests

def check_create_feedback():
    url = 'http://localhost:8080/feedback/create'

    feedback_data = {
        'feedback_id': 1,
        'course_id': 1,
        'student_id': 1,
        'feedback_text': 'Great course! Loved it!'
    }

    # Send POST request with JSON data
    response = requests.post(url, json=feedback_data)

    # Check if request was successful
    if response.status_code == 201:
        # Parse response JSON
        result = response.json()
        message = result.get('message')
        if message:
            print('Feedback created successfully!')
        else:
            print('Failed to create feedback.')
    else:
        print('Request failed with status code:', response.status_code)

def get_feedback():
    url = 'http://localhost:8080/feedback/1'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        feedback = response.json()
        if feedback:
            print('Feedback found:')
            print(feedback)
        else:
            print('Feedback not found.')
    else:
        print('Request failed with status code:', response.status_code)

def update_feedback():
    url = 'http://localhost:8080/feedback/1'

    # changed feedback_text to 'Updated feedback text'
    feedback_data = {
        'course_id': 1,
        'student_id': 1,
        'feedback_text': 'Updated feedback text'
    }

    # Send PUT request with JSON data
    response = requests.put(url, json=feedback_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        message = result.get('message')
        if message:
            print('Feedback updated successfully!')
        else:
            print('Failed to update feedback.')
    else:
        print('Request failed with status code:', response.status_code)

def delete_feedback():
    url = 'http://localhost:8080/feedback/1'

    # Send DELETE request
    response = requests.delete(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        message = result.get('message')
        if message:
            print('Feedback deleted successfully!')
        else:
            print('Failed to delete feedback.')
    else:
        print('Request failed with status code:', response.status_code)

def list_feedback_by_course():
    url = 'http://localhost:8080/feedback/course/1'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        feedbacks = response.json()
        if feedbacks:
            print('Feedbacks found for course 1:')
            print(feedbacks)
        else:
            print('No feedbacks found for course 1.')
    else:
        print('Request failed with status code:', response.status_code)

def list_feedback_by_student():
    url = 'http://localhost:8080/feedback/student/1'

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        feedbacks = response.json()
        if feedbacks:
            print('Feedbacks found for student 1:')
            print(feedbacks)
        else:
            print('No feedbacks found for student 1.')
    else:
        print('Request failed with status code:', response.status_code)

if __name__ == '__main__':
    check_create_feedback()
    # get_feedback()
    # update_feedback()
    # delete_feedback()
    # list_feedback_by_course()
    # list_feedback_by_student()