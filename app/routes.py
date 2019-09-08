from flask import render_template
from app import app
from app import socketio

@app.route('/')
def index():
    return render_template('index.html', title='QuiteLive Dashboard')

@app.route('/info')
def info():
    return render_template('info.html', title='About QuiteLive')

@socketio.on('message')
def event(message):
    print("Message: " + str(message))

@socketio.on('frame')
def event(frame):
    print("Message: " + str(frame))