"""
WE ARE GOING TO MAKE A DOCUMENT SCANNER
---------------------------------------

LOGIC:
- Scan for rectangle sheet with Contour detection and identify the four corners
- Warp the document

CONS:
- ONLY WORKS ON CONTRASTING BACKGROUNDS.
- MIGHT DETECT WRONG PART OF PAPER

"""

import cv2
import numpy as np
from sqlalchemy import true

height = 750
width = 500
img = cv2.imread("images/image4.jpg") # using image coz my webcam sucks :(
img = cv2.resize(img, (width, height))    # change (width, height) accordingly with different images

# initializing warped img
warped = np.zeros_like(img)

# detecting edges
blur = cv2.GaussianBlur(img, (5,5), 2)
canny = cv2.Canny(blur, 200, 200)
dilate = cv2.dilate(canny, (5,5), iterations=5)

# detecting shapes and isolating a rectangle
contour, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contour:
    if cv2.contourArea(cnt) > 50:
        corners = cv2.approxPolyDP(cnt, 50, True)   # corner points array shape (4,1,2)

        if len(corners) == 4:
            corners = np.reshape(corners, (4,2))

            # finding corners in correct order
            min = 999999999
            max = 0
            origin = [0,0]
            right_of_origin = [0,0]
            down_of_origin = [0,0]
            diagonal = [0,0]

            # identifying origin and diagonals
            for x,y in corners:
                if x + y <= min:
                    origin = [x, y]
                    min = x + y
                if x + y >= max:
                    diagonal = [x, y]
                    max = x + y

            # identifying other points
            for x,y in corners:
                if [x,y] != diagonal:
                    if [x,y] != origin:
                        if y > x:
                            down_of_origin = [x, y]
                if [x,y] != diagonal:
                    if [x,y] != origin:
                        if x > y:
                            right_of_origin = [x, y]
                
            cropPoints = np.array([origin, right_of_origin, diagonal, down_of_origin], np.float32)  # crop points
            newPoints = np.array([[0,0], [width, 0], [width, height], [0, height]], np.float32)     # destination points

            matrix = cv2.getPerspectiveTransform(cropPoints, newPoints)                             # perspective matrix
            warped = cv2.warpPerspective(img, matrix, (width, height))                              # warped image

            rectangle = cv2.polylines(img, [corners], True, (0,0,255), 2)                           # rectangle on image
            
            


cv2.imshow("warped", warped)
cv2.imshow("image", img)
cv2.waitKey(0)