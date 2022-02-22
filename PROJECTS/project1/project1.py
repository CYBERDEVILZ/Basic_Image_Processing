# WE ARE GOING TO MAKE A SKRIBBLER USING OPENCV

"""
    DETECT ORANGE PEN BY MASKING AND CONTOUR DETECTION.
    WHEREVER THE MID OF THE CONTOUR IS, DRAW CIRCLE ON THE IMAGE
    MAKE SURE THE CIRCLES PERSIST.
"""

import cv2
from cv2 import FILLED
import numpy as np

vid = cv2.VideoCapture(0)

def onChange(*args):
    pass

# creating trackbars (dev purpose)
cv2.namedWindow("trackbars")
cv2.createTrackbar("minHSV", "trackbars", 0, 180, onChange)
cv2.createTrackbar("maxHSV", "trackbars", 180, 180, onChange)
cv2.createTrackbar("minSat", "trackbars", 0, 255, onChange)
cv2.createTrackbar("maxSat", "trackbars", 255, 255, onChange)
cv2.createTrackbar("minVal", "trackbars", 0, 255, onChange)
cv2.createTrackbar("maxVal", "trackbars", 255, 255, onChange)

board = np.zeros((500,500,3), np.uint8)
board[:] = (255,255,255)

while True:
    success, frame = vid.read()

    # getting the trackbar positions (dev purpose)
    minHSV = cv2.getTrackbarPos("minHSV", "trackbars")  # 0
    maxHSV = cv2.getTrackbarPos("maxHSV", "trackbars")  # 15
    minSat = cv2.getTrackbarPos("minSat", "trackbars")  # 94
    maxSat = cv2.getTrackbarPos("maxSat", "trackbars")  # 239
    minVal = cv2.getTrackbarPos("minVal", "trackbars")  # 215
    maxVal = cv2.getTrackbarPos("maxVal", "trackbars")  # 255

    lowerb = np.array([0, 94, 215])
    upperb = np.array([15, 239, 255])

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, lowerb, upperb)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.circle(board, (x+w//2, y), 5, (0,255,0), thickness=cv2.FILLED)

    cv2.imshow("camera", frame)
    cv2.imshow("board", board)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) == ord('q'):
        break
