from flask import render_template
from app import app
from app import socketio

from PIL import Image
from io import BytesIO
import base64

import cv2

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
    print('Frame Recieved; decoding...')
    frame = frame.split(",")[1]
    image = base64_to_pil_image(frame)
    image.save("pic.jpeg")
