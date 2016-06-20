#!/usr/bin/env python
from flask import Flask, render_template, Response, send_from_directory, jsonify, request, g
import serial

# emulated camera
from camera import Camera

from classes.TrackControl import TrackControl
import serialDevice

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

ser = serial.Serial(serialDevice.DEV, 9600)

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control', methods=['POST'])
def control():
    trackControl = getattr(g, '_trackControl', None)
    if trackControl is None:
        trackControl = g._trackControl = TrackControl(0,0)

    trackControl.setLeft(int(request.form.get('left')))
    trackControl.setRight(int(request.form.get('right')))

    ser.write(trackControl.getSerialMessage())

    return jsonify(left=trackControl.getLeft(),
        right=trackControl.getRight())

@app.route('/control', methods=['GET'])
def get_control():
    trackControl = getattr(g, '_trackControl', None)
    if trackControl is None:
        trackControl = g._trackControl = TrackControl(0,0)

    return jsonify(left=trackControl.getLeft(),
        right=trackControl.getRight())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
