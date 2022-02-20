import cv2
import numpy as np

img = cv2.imread(r"assets\card.png")
cropPoints = np.array([[626,232], [901,319], [775,646], [482,544]], np.int32) # pixels required to crop the image
np.reshape(cropPoints, (-1,1,2))    # important for drawing poly
cv2.polylines(img, [cropPoints], True, (0,255,0), 5)    # draw a rectangle around the area to be wrapped to perspective

cropPoints = np.array([[626,232], [901,319], [775,646], [482,544]], np.float32)

width = 250
height=350
newPoints = np.array([[0,0],[width,0],[width,height],[0,height]], np.float32) # new perspective points for the image
perspectiveMatrix = cv2.getPerspectiveTransform(cropPoints, newPoints)  # creating perspective matrix

newImage = cv2.warpPerspective(img, perspectiveMatrix, (width,height))  # applying image warp

cv2.imshow("normal", img)
cv2.imshow("new Image", newImage)
cv2.waitKey(0)

"""
NOTES

DRAWING POLYGON
---------------
Create an INT32 numpy array with the polygon points.
Reshape them to (-1 X 1 X 2).
while passing the array, make sure you enclose it in [].

CREATEING PERSPECTIVE MATRIX
----------------------------
The points should be in float32.






"""