from flask import Flask
from flask_socketio import SocketIO
# Require flask-socketio
# Require eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

<<<<<<< HEAD
from app import app
=======
if __name__ == '__main__':
    socketio.run(app, debug=True)

from app import routes
>>>>>>> frontend
