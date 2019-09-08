from flask import render_template, session
from app import app
from app import socketio
import eventlet

from PIL import Image
from io import BytesIO
import base64

import cv2
import numpy

import os
import shutil

from app import sendOp
from app import hashFile

stream_path = './stream/'


def pil_image_to_base64(pil_image):
    buf = BytesIO()
    pil_image.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue())


def base64_to_pil_image(base64_img):
    return Image.open(BytesIO(base64.b64decode(base64_img)))

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

    frame = frame.split(",")[1]
<<<<<<< Updated upstream
    img = base64_to_pil_image(frame)

    session['vidout'].write(numpy.array(img)[:, :, ::-1].copy())

@socketio.on('stream-start')
def streamStart(packet):
    session['vidout'] = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 24.0, (640,480))
=======
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
>>>>>>> Stashed changes
    image = base64_to_pil_image(frame)
    image.save(stream_path + str(session['count']) + ".jpg")
    if os.path.exists(stream_path + str(session['count']) + ".jpg"):
        session['count'] = session['count'] + 1
<<<<<<< Updated upstream

@socketio.on('stream-start')
def streamStart(packet):
    print("STREAM STARTING")
=======

@socketio.on('stream-start')
def streamStart(packet):
    print("STREAM STARTING")
=======
<<<<<<< HEAD
    img = base64_to_pil_image(frame)

    session['vidout'].write(numpy.array(img)[:, :, ::-1].copy())

@socketio.on('stream-start')
def streamStart(packet):
    session['vidout'] = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 24.0, (640,480))
=======
    image = base64_to_pil_image(frame)
    image.save(stream_path + str(session['count']) + ".jpg")
    if os.path.exists(stream_path + str(session['count']) + ".jpg"):
        session['count'] = session['count'] + 1
    if session['startFlag']:
        hashOfFirstFrame = hashFile.sha256sum(stream_path + str(session['count'] - 1) + ".jpg")
        session['FirstFrameHash'] = sendOp.sendOpTx(hashOfFirstFrame)


@socketio.on('stream-start')
def streamStart(packet):
    print("STREAM STARTING")
    session['startFlag'] = True
>>>>>>> Stashed changes
>>>>>>> Stashed changes
    try:
        if os.path.exists(stream_path):
            shutil.rmtree(stream_path)
        os.mkdir(stream_path)
    except OSError:
        print(OSError)

    session['count'] = 0
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
=======
>>>>>>> nova
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes

@socketio.on('stream-end')
def streamEnd(packet):
    print("STREAM ENDING")
<<<<<<< Updated upstream
    session['vidout'].release()
=======
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
>>>>>>> Stashed changes
    img1 = cv2.imread(stream_path + '0.jpg')

    height, width, layers = img1.shape
    vidout = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 24.0, (640,480))
<<<<<<< Updated upstream
=======
=======
<<<<<<< HEAD
    session['vidout'].release()
=======
    img1 = cv2.imread(stream_path + '0.jpg')

    vidout = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 24.0, (640, 480))
>>>>>>> Stashed changes
>>>>>>> Stashed changes
    vidout.write(img1)
    for i in range(1, session['count']):
        #print(stream_path + str(i) + '.jpg')
        framed = cv2.imread(stream_path + str(i) + '.jpg')
        vidout.write(framed)

<<<<<<< Updated upstream
    cv2.destroyAllWindows()
    vidout.release()
=======
<<<<<<< Updated upstream
    cv2.destroyAllWindows()
    vidout.release()
=======
    vidout.release()
>>>>>>> nova
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
