import requests

def recommend_courses():
    url = 'http://localhost:8080/recommend_courses'  # Adjust the port and route as necessary

    # Prepare the data based on user inputs you specified
    course_data = {
        'roll_number': '2021103425',
        'course_type': 'CS',  # Assuming 5 corresponds to Computer Science
        'user_preferences': [
            -0.1111,  # -(1/9) for difficulty
            9, 9, 9, 9, 9, 9, 9, 9, 9  # Other preferences all set to 9
        ],
        'feature_labels': [
            'Difficulty', 'Time commitment', 'New learning', 'Structure quality', 
            'Material quality', 'Assignment quality', 'Exam quality', 'Expectation alignment', 
            'Instructor quality', 'Recommendation Likelihood'
        ],
        'feature_keys': [
            "How would you rate the difficulty of the course?",
            "How would you rate the extent of time commitment required for the course?",
            "How much would you say you learned from the course?",
            "How well do you think the course was structured?",
            "How would you rate the quality of the course material?",
            "How would you rate the quality of the assignments?",
            "How would you rate the quality of the exams?",
            "How well did the course align with your expectations?",
            "How would you rate the quality of your instructor?",
            "How likely are you to recommend this course to your juniors?"
        ]
    }

    # Send POST request with JSON data
    response = requests.post(url, json=course_data)

    # Check if request was successful
    if response.status_code == 200:
        print('Recommendation received successfully!')
        recommendations = response.json()
        print(recommendations)
    else:
        print('Failed to get recommendations. Status code:', response.status_code)

if __name__ == '__main__':
    recommend_courses()
