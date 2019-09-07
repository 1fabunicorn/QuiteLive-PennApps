import threading
import atexit
from flask import Flask
from flask import render_template


POOL_TIME = 5 #Seconds

# variables that are accessible from anywhere
commonDataStruct = {}
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
yourThread = threading.Thread()

def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', title='Home')

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
        with dataLock:
            print("hi")
        # Do your stuff with commonDataStruct Here

        # Set the next thread to happen
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app

app = create_app()