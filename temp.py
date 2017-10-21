import cv2

video_capture = cv2.VideoCapture(0)

while True:
        is_sucessfully_read, img = video_capture.read()
        if(is_sucessfully_read):
            cv2.imshow("Camera Feed", img)
        else:
            print("Cannot read video capture object from %s. Quitting...")% capture
            break
        val = cv2.waitKey(300)
        if val == 27:
            break
