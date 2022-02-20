import black
import cv2
import numpy as np

blackImg = np.zeros((300,300,3), np.uint8)  # black GBR Image

cv2.line(blackImg, (0,0), (blackImg.shape[1],blackImg.shape[0]), (0,255,0), thickness=2)    # Line through the diagonal (green)
cv2.rectangle(blackImg, (0, blackImg.shape[1]//2), (30, 100), (255,0,0), thickness=cv2.FILLED)  # Rectangle (blue-filled)
cv2.circle(blackImg, (150,150), 40, (0,0,255), thickness=2) # Circle (red-outline)
cv2.putText(blackImg, "Opencv Python", (30,100), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,0), 2)  # Text (light blue?)

cv2.imshow("line", blackImg)
cv2.waitKey(0)