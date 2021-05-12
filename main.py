from flask import Flask, render_template, url_for, Response
from camera import Camera
# import cv2
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("HomePage.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == "__main__":
    app.run(debug=True)
    