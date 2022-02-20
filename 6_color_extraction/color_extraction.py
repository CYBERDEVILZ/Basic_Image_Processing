import cv2
import numpy as np

def onChange(*args): # function for trackbar
    pass

cv2.namedWindow("Controllers")  # window for trackbars to be placed
cv2.resizeWindow("Controllers", 600, 250)
cv2.createTrackbar("Hue_min", "Controllers", 0, 179, onChange)      # trackbar to controll Hue_min
cv2.createTrackbar("Hue_max", "Controllers", 179, 179, onChange)    # trackbar to controll Hue_max
cv2.createTrackbar("Sat_min", "Controllers", 0, 255, onChange)      # trackbar to controll Sat_min
cv2.createTrackbar("Sat_max", "Controllers", 255, 255, onChange)    # trackbar to controll Sat_max
cv2.createTrackbar("Val_min", "Controllers", 0, 255, onChange)      # trackbar to controll Val_min
cv2.createTrackbar("Val_max", "Controllers", 255, 255, onChange)    # trackbar to controll Val_max


while True:
    
    # Get the values from the trackbar
    hue_min = cv2.getTrackbarPos("Hue_min", "Controllers")
    hue_max = cv2.getTrackbarPos("Hue_max", "Controllers")
    sat_min = cv2.getTrackbarPos("Sat_min", "Controllers")
    sat_max = cv2.getTrackbarPos("Sat_max", "Controllers")
    val_min = cv2.getTrackbarPos("Val_min", "Controllers")
    val_max = cv2.getTrackbarPos("Val_max", "Controllers")

    # Create array for both lower and upper values
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    img = cv2.imread("assets/zbunker.png")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # HSV = Hue(min: 0, max: 179), Saturation(min:0, max: 255), Value(min: 0, max: 255)

    mask = cv2.inRange(imgHSV, lower, upper)    # creates mask
    extracted = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Extracted", extracted)

    if cv2.waitKey(1) == ord('q'):
        break


"""
VALUES FOR EXTRACTING BLUE COLOR FROM ZBUNKER.PNG
-------------------------------------------------
Hue_min = 84
Hue_max = 92
Sat_min = 0
Sat_max = 255
Val_min = 167
Val_max = 235
"""