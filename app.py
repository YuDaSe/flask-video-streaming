#!/usr/bin/env python
from flask import Flask, render_template, Response, send_from_directory, jsonify, request, g
from flask_socketio import SocketIO, send, emit

# emulated
#from camera import Camera
#import serial_mock as serial

from classes.TrackControl import TrackControl
from classes.TrackManeuver import TrackManeuver
import serialDevice

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
import serial

ser = serial.Serial(serialDevice.DEV, 9600)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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

@socketio.on('maneuver')
def maneuver(maneuver):
    trackControl = getTreackControl()

    tm = TrackManeuver(
        maneuver['track'],
        maneuver['duration'],
        maneuver['delta']
    )

    ser.write(tm.getSerialMessage())

    send(trackControl.to_json(), json=True)

@socketio.on('control_setup')
def control(control):
    trackControl = getTreackControl()

    trackControl.setLeft(control['left'])
    trackControl.setRight(control['right'])

    ser.write(trackControl.getSerialMessage())

    send(trackControl.to_json(), json=True)

@app.route('/control', methods=['GET'])
def get_control():
    trackControl = getTreackControl()

    return jsonify(left=trackControl.getLeft(),
        right=trackControl.getRight())

def getTreackControl():
    trackControl = getattr(g, '_trackControl', None)
    if trackControl is None:
        trackControl = g._trackControl = TrackControl(0,0)

    return trackControl

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True, threaded=True)
    socketio.run(app)
