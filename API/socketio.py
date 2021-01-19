from flask_socketio import *


def socketio_config(application):
    socketio = SocketIO(application, cors_allowed_origins="*")

    @socketio.on('connect')
    def connected():
        print('Connected')

    @socketio.on('disconnect')
    def disconnected():
        print('Disconnected')

    @socketio.on('UserAdded')
    def echo(message):
        emit('userAddedResponse', {'data': message}, broadcast=True)
