import threading
import atexit
from flask import Flask
from flask import render_template
from src import sendOp


POOL_TIME = 5  # Seconds

# variables that are accessible from anywhere
dataStruct = {
    "instruction": [],
    "data": [],
    "return": []
}
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

    def backendProcess():
        global dataStruct
        global yourThread
        with dataLock:
            if not not dataStruct["instruction"]:
                if dataStruct["instruction"] == "sendOpTx":
                    dataStruct["return"] = sendOp.sendOpTx(dataStruct["data"])
                    dataStruct["instruction"] = []
                # No need for using other functions unless we are verifying

            else:
                pass

        # Set the next thread to happen
        yourThread = threading.Timer(POOL_TIME, backendProcess, ())
        yourThread.start()

    def threadInit():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, backendProcess, ())
        yourThread.start()

    # Initiate
    threadInit()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app


app = create_app()