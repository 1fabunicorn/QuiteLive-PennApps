from flask import render_template, session
from app import app
from app import socketio
import threading

from PIL import Image
from io import BytesIO
import base64

import cv2
import os
import shutil

from app import sendOp
from app import hashFile
from app.src import Functions

stream_path = './stream/'
global image_count

def pil_image_to_base64(pil_image):
    buf = BytesIO()
    pil_image.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue())

global bcHash
def returnBlockHash(tx):
    pass

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
    print(session['count'])
    frame = frame.split(",")[1]
    image = base64_to_pil_image(frame)
    image.save(stream_path + str(session['count']) + ".jpg")
    if os.path.exists(stream_path + str(session['count']) + ".jpg"):
        session['count'] = session['count'] + 1
    if session['startFlag']:
        hashOfFirstFrame = hashFile.sha256sum(stream_path + str(session['count'] - 1) + ".jpg")
        print(sendOp.sendOpTx(hashOfFirstFrame))
        session['startFlag'] = False
    # tryHash = sendOp.getBlockHash(session['FirstFrameHash'])
    # if tryHash == "error code: -5\nerror message:\nInvalid or non-wallet transaction id":
    #     pass
    # else:2293d93466d4139b85ac55e6d2cfc2b99a26c61ba9f9e2629904df76709cd443
    #     Functions.bitStringAnd(tryHash, session["FirstFrameHash"])






@socketio.on('stream-start')
def streamStart(packet):
    print("STREAM STARTING")
    try:
        if os.path.exists(stream_path):
            shutil.rmtree(stream_path)
        os.mkdir(stream_path)
    except OSError:
        print(OSError)
    session['startFlag'] = True
    session['count'] = 0

@socketio.on('stream-end')
def streamEnd(packet):
    print("STREAM ENDING")
    img1 = cv2.imread(stream_path + '0.jpg')

    vidout = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 24.0, (640, 480))
    vidout.write(img1)
    for i in range(1, session['count']):
        #print(stream_path + str(i) + '.jpg')
        framed = cv2.imread(stream_path + str(i) + '.jpg')
        vidout.write(framed)
    vidout.release()