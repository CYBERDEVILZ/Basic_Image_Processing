import cv2
import numpy as np

img = cv2.imread("assets/shapes.png")
imgCopy = img.copy()
imgBlur = cv2.GaussianBlur(img, (5,5), 0)   # blur the image to hide fine grain details
imgCanny = cv2.Canny(imgBlur, 150,150)      # edge detection on blurred image

blankSlate = np.zeros((500,800,3), np.uint8)

# Contour related processing
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    cntArea = cv2.contourArea(cnt)                                  # finds the area of the contour (px-squared)
    if cntArea > 500:                                               # to prevent small fine grained shapes to be detected
        peri = cv2.arcLength(cnt, True)                             # finds perimeter of contour
        corners = cv2.approxPolyDP(cnt, 0.02*peri, True)            # Tries to find the corner points of contours and returns a numpy ndarray
        cv2.polylines(blankSlate, [corners], True, (0,255,0), 3)    # drawing the corners on black screen
        cv2.drawContours(imgCopy, cnt, -1, (0, 255, 0), 5)          # draws contour
        print("Area:" + str(cntArea))
        print("Perimeter:" + str(peri))
        
        
        


cv2.imshow("original", img)
cv2.imshow("canny", imgCanny)
cv2.imshow("contour", imgCopy)
cv2.imshow("drawing Board", blankSlate)
cv2.waitKey(0)

"""
NOTES

HOW TO FIND CONTOURS (SHAPE DETECTION)
--------------------------------------
1. Always blur images before processing to remove finer grains
2. Image should have black and white contrast, hence canny edge detection
3. Use findContours() method. It has two positional arguments:
    - contour retrieval mode
    - contour approximation method
   This method returns a tuple (contour{which is a list}, hierarchy{no need to know})
4. use cv2.drawContour() to draw the contours
"""