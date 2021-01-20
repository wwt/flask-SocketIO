from flask import Flask, jsonify, request, Response
from flask_socketio import *
from flask_cors import CORS

from UserModel import *
from settings import *

import json

def validUserObject(userObject):
    if ("firstName" in userObject and
        "lastName" in userObject and
        "office" in userObject and
        "email" in userObject and
            "mobile" in userObject):
        return True
    else:
        return False

# SocketIO 
socketio = SocketIO(app, cors_allowed_origins="*")

# app Routes

@app.route('/users')
def get_users():
    return jsonify({'users': User.get_all_users()})


@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    if(validUserObject(request_data)):
        User.add_user(request_data['firstName'], request_data['lastName'],
                      request_data['office'], request_data['email'], request_data['mobile'])
        return Response("", 201, mimetype='applciation/json')
    else:
        invalidUserObjectErrorMsg = {
            "error": "Invalid user object passed in request"
        }
        return Response(json.dumps(invalidUserObjectErrorMsg), status=400, mimetype='applciation/json')


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    request_data = request.get_json()
    User.update_user(id, request_data['firstName'], request_data['lastName'],
                     request_data['office'], request_data['email'], request_data['mobile'])
    return Response("", 201, mimetype='applciation/json')


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if(User.delete_user(id)):
        return Response("", status=204)

    return Response("", status=404, mimetype='application/json')

# SocketIO Events
@socketio.on('connect')
def connected():
    print('Connected')

@socketio.on('disconnect')
def disconnected():
    print('Disconnected')

@socketio.on('UserAdded')
def userAdded(message):
    print('User Added')
    emit('userAddedResponse', {'data': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
