from flask import Flask
from flask_socketio import SocketIO
# Require flask-socketio
# Require eventlet

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from app import app
if __name__ == '__main__':
    socketio.run(app, debug=False)

from app import routes
