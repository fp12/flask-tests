from flask_socketio import SocketIO, emit


socketio = SocketIO()


@socketio.on('status', namespace='/events')
def on_status(message):
    print('connected status', {'status': message['status']})
    emit('status', {'status': 'Connected user', 'userid': None})
