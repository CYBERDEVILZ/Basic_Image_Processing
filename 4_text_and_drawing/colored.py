import cv2
import numpy as np

blackImg = np.zeros((512,512,3), np.uint8)   # creates a black GBR Image
blueImg = np.zeros((512,512,3), np.uint8)
blueImg[:] = (255,0,0)  # fill all rows with (255,0,0) value

cv2.imshow("black image", blackImg)
cv2.imshow("blue image", blueImg)
cv2.waitKey(0)