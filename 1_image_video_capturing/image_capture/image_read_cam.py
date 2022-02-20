
"""

    REFER TO VIDEO CAPTURE SECTION FIRST!

"""

import cv2

img = cv2.VideoCapture(0)

while True:
    success, frame = img.read()
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite("./webcam.png", frame)
        break