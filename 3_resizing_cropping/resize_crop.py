import cv2

vid = cv2.VideoCapture(0)
vid.set(3, 256)
vid.set(4, 144)

while True:
    success, frame = vid.read()
    resizedFrame = cv2.resize(frame, (1000,144))    # resizing (width, height)
    cv2.imshow("normal", frame)
    cv2.imshow("stretched", resizedFrame)
    cv2.imshow("cropped", frame[:120, 125:])    # cropping (numpy ndarray)
    if cv2.waitKey(1) == ord('q'):
        break


"""
IMAGE MATRIX FOR (256 x 144 x 3) (height x width x channel)
-----------------------------------------------------------
[
    [                              _
          B    G    R               |
        [123   0   200]             |
        [121   0   200]             |
        [123   0   200]             |   First Row 
        .                           |
        .                           |
        .                           |
        144 total values            |
    ]                              -'

    [                              _
          B    G    R               |
        [123   0   200]             |
        [121   0   200]             |
        [123   0   200]             |   Second Row 
        .                           |
        .                           |
        .                           |
        144 total values            |
    ]                              -'
    .
    .
    .                              
    256 total values               
]
"""