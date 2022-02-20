
"""
This particular code guides you through reading an image from
a folder and displaying it to the screen
"""

import cv2

img = cv2.imread(r"assets\zbunker.png")   # read image from file
cv2.imshow(winname="Window Name", mat=img)  # show the image
cv2.waitKey(0)  # waits infinitely until a key is pressed (whic is returned) or n millisec has completed
