import requests


def check_signup():
    url = 'http://localhost:8080/sign_up/instructor'

    instructor_data = {
        'instructor_id': 122034512,
        'name': 'John Doe',
        'email': 'johnee1@example.com',
    }

    # Send POST request with JSON data
    response = requests.post(url, json=instructor_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        success = result.get('success')
        if success:
            print('Instructor created successfully!')
        else:
            print('Failed to create instructor.')
    else:
        print('Request failed with status code:', response.status_code)



def login():
    url = 'http://localhost:8080/login/instructor'

    instructor_data = {
        'instructor_id': 122034512,
    }

    # Send POST request with JSON data
    response = requests.get(url, json=instructor_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        instructor = result.get('instructor')
        if instructor is not None:
            print('Instructor login successfully!')
            print(instructor)
        else:
            print('Failed to login instructor.')
    else:
        print('Request failed with status code:', response.status_code)


def update_instructor():
    url = 'http://localhost:8080/update/instructor'

    # changed email to e -> y
    instructor_data = {
        'instructor_id': 122034512,
        'name': 'John Doe',
        'email': 'johnyy1@example.com',
    }

    # Send POST request with JSON data
    response = requests.post(url, json=instructor_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        success = result.get('success')
        if success:
            print('Instructor update successfully!')
        else:
            print('Failed to update instructor.')
    else:
        print('Request failed with status code:', response.status_code)


def delete():
    url = 'http://localhost:8080/delete/instructor'

    instructor_data = {
        'instructor_id': 122034512,
    }

    # Send GET request with JSON data
    response = requests.get(url, json=instructor_data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        result = response.json()
        success = result.get('success')
        if success:
            print('Instructor deleted successfully!')
        else:
            print('Failed to delete instructor.')
    else:
        print('Request failed with status code:', response.status_code)



if __name__ == '__main__':

    # 1. Test sign_up()
    check_signup()

    # 2. Test login()
    login()

    # 3. Test update_instructor()
    update_instructor()

    # 4. Test delete()
    delete()