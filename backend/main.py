from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi

USERNAME = 'username'
PASSWORD = 'password'
# @TODO KEEP THIS PRIVATE
URI = "mongodb+srv://fazilibrahim:password@gh1.krlzpmw.mongodb.net/?retryWrites=true&w=majority"

# Flask app object
app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient(URI, server_api=ServerApi('1'))
database = client['grade-hero']

# User routes
@app.route('/register', methods=['POST'])
def register_user():
    user_collection = database['users']
    username = request.json.get(USERNAME)

    user_exists = user_collection.find_one({'username': username})
    if user_exists:
        return jsonify(message='Username already exists'), 409
    
    user_collection.insert_one(request.json)
    return jsonify(message='User registered successfully'), 200

@app.route('/login', methods=['POST'])
def login_user():
    user_collection = database['users']
    username = request.json.get(USERNAME)
    password = request.json.get(PASSWORD)
    user_exists = user_collection.find_one({'username': username, 'password': password})
    if user_exists:
        return jsonify(message='Login Successful'), 200
    else:
        return jsonify(message='Username and/or password is incorrect or does not exist'), 401

# Course Routes

@app.route('/addcourse', methods=['POST'])
def add_course():
    pass

# Health Check Routes

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/ping-mongodb', methods=['GET'])
def ping_mongodb():
    try:
        # Ping MongoDB
        client.admin.command('ping')

        # If the ping is successful, return a success message
        return jsonify(status='MongoDB is alive')

    except Exception as e:
        # If there is an error during the ping, return an error message
        return jsonify(status='MongoDB is not accessible', error=str(e)), 500
  
  
if __name__ == '__main__':
    app.run()