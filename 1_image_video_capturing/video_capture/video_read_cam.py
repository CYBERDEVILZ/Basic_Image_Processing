import cv2

vid = cv2.VideoCapture(0)   # 0 means default cam
vid.set(3,640)  # set width
vid.set(4,480)  # set height

while True:
    success, frame = vid.read()
    cv2.imshow("WebCam", frame)
    if(cv2.waitKey(60) == ord('q')):
        break