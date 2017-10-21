import cv2

class VideoCamera():
    def __init__(self, camera = -1):
        self.video = cv2.VideoCapture(camera)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if success:
            return image
        else:
            raise(Exception('Frame not found'))

    def get_bytes(self):
        image = self.get_frame()
        ret, jpeg = cv2.imencode('.jpg', image)
        if ret:
            return jpeg.tobytes()
        else:
            raise(Exception('Bytes not found'))

    def get_base64(self):
        return b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + self.get_bytes() + b'\r\n\r\n'
