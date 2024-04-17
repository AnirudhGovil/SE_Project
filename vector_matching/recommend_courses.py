# We can use KNN to recommend courses to students based on their preferences

import numpy as np
import pickle
from sklearn.neighbors import NearestNeighbors
import json

# Load the aggregated course features
with open('SE_Project/data_generation/course_features_aggregated.pkl', 'rb') as f:
    course_features_aggregated = pickle.load(f)

categories = ['SC', 'MA', 'EE', 'HU', 'CS']
filter  = int(input('What type of course are you looking for?\n [1 : Science, 2 : Mathematics, 3 : Electrical Engineering, 4 : Humanities, 5 : Computer Science]: '))
filter = categories[filter-1]
# Allow the user to enter their preferences
alpha = int(input('What difficulty are you willing to tolerate? (1-10): '))
beta = int(input('How much time can you commit to the course? (1-10): '))
gamma = int(input('How important is it to you to learn something new from the course? (1-10): '))

# Filter the courses based on delta
course_features_filtered = {course: course_features_aggregated[course] for course in course_features_aggregated if course[:2] == filter}
# Only take the latest year's courses
course_features_filtered = {course: course_features_filtered[course] for course in course_features_filtered if course[2:4] == '23'}

# Create a vector of the user's preferences
user_preferences = np.array([alpha, beta, gamma])

# The correspond to the 0th, 1st and 2nd elements of the aggregated course features
X = np.array([course_features_filtered[course][:3] for course in course_features_filtered])

# Fit a KNN model
knn = NearestNeighbors(n_neighbors=3)

# Fit the model
knn.fit(X)

# Find the nearest neighbors
_, indices = knn.kneighbors(user_preferences.reshape(1, -1))

with open('SE_Project/data_generation/courses.json') as f:
    courses = json.load(f)

# Create a courses dictionary with the course id as the key
courses = {course['ID']: course for course in courses}

# Print the recommended courses
print('\nRecommended courses:\n')
for index in indices[0]:
    course_id = list(course_features_filtered.keys())[index]
    print(courses[course_id]['Name'])
    print('Course ID: ', course_id)
    print('Difficulty: ', course_features_filtered[course_id][0])
    print('Time commitment: ', course_features_filtered[course_id][1])
    print('Learning Staisfaction: ', course_features_filtered[course_id][2])
    print('')













