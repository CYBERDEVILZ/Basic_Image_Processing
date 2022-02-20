import cv2

vid = cv2.VideoCapture(0)

while True:
    success, frame = vid.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(r"assets\haarcascades\haarcascade_frontalface_default.xml") # instantiating cascade
    faces = faceCascade.detectMultiScale(frameGray)  # detecting features and returns x,y,w,h

    eyeCascade = cv2.CascadeClassifier(r"assets\haarcascades\haarcascade_eye_tree_eyeglasses.xml")
    eyes = eyeCascade.detectMultiScale(frameGray)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, "FACE", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow("face detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break