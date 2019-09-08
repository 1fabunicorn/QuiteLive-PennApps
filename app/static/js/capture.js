/*
 *  Copyright (c) 2015 The WebRTC project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree.
 */
'use strict';

// Put variables in global scope to make them available to the browser console.
const constraints = window.constraints = {
    audio: false,
    video: true
};

let namespace = "/stream";
let video = document.querySelector("#camera-window");
let canvas = document.querySelector("#canvasElement");
let ctx = canvas.getContext('2d');

var localMediaStream = null;
var eventInterval = null;
var socket = null;

function handleSuccess(stream) {
    const video = document.querySelector('video');
    const videoTracks = stream.getVideoTracks();
    console.log('Got stream with constraints:', constraints);
    console.log(`Using video device: ${videoTracks[0].label}`);
    window.stream = stream; // make variable available to browser console
    localMediaStream = stream;
    video.srcObject = stream;
}

function handleError(error) {
    if (error.name === 'ConstraintNotSatisfiedError') {
        let v = constraints.video;
        errorMsg(`The resolution ${v.width.exact}x${v.height.exact} px is not supported by your device.`);
    } else if (error.name === 'PermissionDeniedError') {
        errorMsg('Permissions have not been granted to use your camera and ' +
            'microphone, you need to allow the page access to your devices in ' +
            'order for the demo to work.');
    }
    errorMsg(`getUserMedia error: ${error.name}`, error);
}

function errorMsg(msg, error) {
    console.error(error);
}

async function init(e) {
    try {
        document.getElementById("showVideo").classList.add("disabled");
        document.getElementById("showVideo").disabled = true;
        document.getElementById("startCapture").classList.remove("d-none");
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
    } catch (e) {
        handleError(e);
    }
}

function sendFrame() {
    if (!localMediaStream){
        console.log("Error: No media detected!");
        return;
    }

    ctx.drawImage(video, 0, 0, 640, 480, 0, 0, 640, 480);

    let dataURL = canvas.toDataURL('image/jpeg');
    socket.emit('frame', dataURL);
}

function setStatusButton(status) {
    let button_start = document.querySelector('#startCapture');
    let button_stop = document.querySelector('#stopCapture');

    if(status) {
        button_start.classList.remove('d-block');
        button_start.classList.add('d-none');
        button_stop.classList.remove('d-none');
        button_stop.classList.add('d-block');
    } else {
        button_start.classList.remove('d-none');
        button_start.classList.add('d-block');
        button_stop.classList.remove('d-block');
        button_stop.classList.add('d-none');
    }

}

function startStream(e) {
    // First, change the button
    setStatusButton(true);

    // Initiate interval
    socket = io();
    socket.on('connect', function() {
        socket.emit('stream-start', {});
    });

    setInterval(function () {
        sendFrame();
    }, 50);
}

function stopStream(e) {
    setStatusButton(false);
    socket.emit('stream-end', {});
    socket.close();
    clearInterval(eventInterval);
}

document.querySelector('#showVideo').addEventListener('click', e => init(e));

document.querySelector('#startCapture').addEventListener('click', e => startStream(e));
document.querySelector('#stopCapture').addEventListener('click', e => stopStream(e));