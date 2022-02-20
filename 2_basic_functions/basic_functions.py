import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)   # for image dilation and erosion

vid = cv2.VideoCapture(0)
vid.set(3, 256) # setting width to 256px
vid.set(4, 144)  # setting height to 144px

while True:
    success, frame = vid.read()

    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # greyscaling
    blurredFrame = cv2.GaussianBlur(frame, ksize=(45,45), sigmaX=0, sigmaY=0)   # blurred
    edgeDetectionFrame = cv2.Canny(frame, 100, 100) # edge detection
    dilatedFrame = cv2.dilate(edgeDetectionFrame, kernel)    # dilation
    erodedFrame = cv2.erode(dilatedFrame, kernel)    # erosion

    cv2.imshow("normal", frame)
    cv2.imshow("greyscaled", greyframe)
    cv2.imshow("blurred", blurredFrame)
    cv2.imshow("edge detection", edgeDetectionFrame)
    cv2.imshow("dilated", dilatedFrame)
    cv2.imshow("eroded", erodedFrame)
    if cv2.waitKey(1) == ord('q'):
        break

"""
NOTES

IT'S GBR NOT RGB!
-----------------
OpenCV reads an image in GBR Format and not in RGB Format

GAUSSIAN BLUR
-------------
ksize parameter of GaussianBlur method takes in only odd and positive number tuples
(x,y). The greater the value, the greater the blur. The first number is the kernel
width, the second number is the kernel height.
If x > y, the image will be blurred and will appear as if it is stretched along the width.
If y > x, the image will be blurred and will appear as if it is stretched along the height.

sigmaX and sigmaY are standard deviation in X and Y direction respectively.

CANNY EDGE DETECTION
--------------------
The second and third parameter of Canny method is threshold1 and threshold2.
threshold1 = minValue for hysterisis thresholding
threshold2 = maxValue for hysterisis thresholding

Hysteris Thresholding. (High level concept, dont worry if you dont understand)
If the intensity gradient of a curve is greater than maxVal, then it is considered a 
"sure-edge". If a curve is connected to a "sure-edge" curve,  and it is below maxVal, 
and above minVal, it is still considered to be an edge.
If the intensity gradient of a curve is above minVal but less than maxVal, and it is
not connected to any "sure-edge" curve, then it is not considered an edge.

IMAGE DILATION
--------------
Normally used with edge detection to increase the thickness of the edges. It results
in the pixel with maximum size in a neighbouring region to become more thicker.

The second parameter in dilate method is kernel, which is an (n x n) matrix with ones.

"iteration" parameter repeats the above process with the kernel n times.

IMAGE EROSION
-------------
Normally used with edge detection to decrease the thickness of the edges. It results
in the pixel with maximum size in a neighbouring region to become more thinner.

The second parameter in dilate method is kernel, which is an (n x n) matrix with ones.

"iteration" parameter repeats the above process with the kernel n times.
"""