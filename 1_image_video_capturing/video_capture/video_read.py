import cv2

vid = cv2.VideoCapture(r"assets\intro.mp4")   # captures video from file

while True:
    success, frame = vid.read()  # reads video frame by frame and returns tuple (success, frame)
    cv2.imshow("Video", frame)
    if (cv2.waitKey(1) & 0xFF)== ord('q'):    # refer the annotation below
        break


"""
QUESTION
So, what is this code => `cv2.waitKey(1) & 0xff`
Why do we perform a bitwise operation with 0xff (255 bits or 11111111)?

ANSWER
We want our program to close when we press the key "q" (remember it is lowercase).

Now cv2.waitKey(n) is either going to wait for n seconds or its gonna wait till
you press any key. If you press any key then the "32 bit integral value" of that key is 
returned. Which means 32 bits will be used to represent number. Now, ord() function
returns an 8 bit value. Hence, by masking the 32 bits with 0xff or 11111111, we get
the last 8 bits instead of all 32 bits. 

IN REALITY, EVEN IF WE EXCLUDE 0XFF, IT WILL STILL WORK.
BECAUSE:

00000000000000000000000000001111 == 00001111
|____________32bit_____________|    |_8bit_|

"""