import requests


def check_signup():
    url = 'http://localhost:8080/sign_up/student'

    student_data = {
        'student_id': 122034512,
        'name': 'John Doe',
        'email': 'johnee1@example.com',
        'roll_number': '122034512'
    }

    # Send POST request with JSON data
    response = requests.post(url, json=student_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        success = result.get('success')
        if success:
            print('Student created successfully!')
        else:
            print('Failed to create student.')
    else:
        print('Request failed with status code:', response.status_code)



def login():
    url = 'http://localhost:8080/login/student'

    student_data = {
        'student_id': 122034512,
    }

    # Send POST request with JSON data
    response = requests.get(url, json=student_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        student = result.get('student')
        if student is not None:
            print('Student login successfully!')
            print(student)
        else:
            print('Failed to login student.')
    else:
        print('Request failed with status code:', response.status_code)


def update_student():
    url = 'http://localhost:8080/update/student'

    # changed email to e -> y
    student_data = {
        'student_id': 122034512,
        'name': 'John Doe',
        'email': 'johnyy1@example.com',
        'roll_number': '122034512'
    }

    # Send POST request with JSON data
    response = requests.post(url, json=student_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        success = result.get('success')
        if success:
            print('Student update successfully!')
        else:
            print('Failed to update student.')
    else:
        print('Request failed with status code:', response.status_code)


def delete():
    url = 'http://localhost:8080/delete/student'

    student_data = {
        'student_id': 122034512,
    }

    # Send GET request with JSON data
    response = requests.get(url, json=student_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        success = result.get('success')
        if success:
            print('Student deleted successfully!')
        else:
            print('Failed to delete student.')
    else:
        print('Request failed with status code:', response.status_code)



if __name__ == '__main__':

    # 1. Test sign_up()
    check_signup()

    # 2. Test login()
    login()

    # 3. Test update_student()
    update_student()

    # 4. Test delete()
    delete()