from camera import VideoCamera
from logic import PrinterGPIO
from flask import Flask, render_template, Response, request
from time import sleep

ON = False

ON_MESSAGE = "Power off"
OFF_MESSAGE = "Turn on"

GPIO = PrinterGPIO()

app = Flask(__name__)

#CAM = 

@app.route('/')
def index():
    global ON
    if ON:
        message = ON_MESSAGE
    else:
        message = OFF_MESSAGE
    btn1 = ON
    return render_template('index.html', message = message, btn1 = btn1)

def gen(camera):
    while True:
        yield(camera.get_base64())

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/test', methods=['POST'])
def test():
    global ON
    ON = not ON
    if ON:
        message = ON_MESSAGE
    else:
        message = OFF_MESSAGE
    btn1 = ON
    GPIO.setNewState(ON)
    return render_template('index.html', message = message, btn1 = btn1)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
