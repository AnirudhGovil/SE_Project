# use flask to  create endpoint for login and register

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app,supports_credentials=True)

# allow cross origin requests


# Dummy data for users

users = [
    {
        'email': 'raj@gmail.com',
        'password': '1234'
    },
    {
        'email': 'hari@gmail.com',
        'password': '1234'
    }
]

@app.route('/login/', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    # data = request.data
    # print(data)
    data = request.get_json()
    print(data)
    email = data.get('email')
    password = data.get('password')

    print(email, password)

    for user in users:
        if user['email'] == email and user['password'] == password:
            return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Login failed'})

    return jsonify({'message': 'Login successful'})




@app.route('/signup/', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return jsonify({'email': email, 'password': password})

if __name__ == '__main__':

    app.run(port=5000, debug=True)

# Run the backend server

