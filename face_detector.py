import cv2

cascPath = "src\\face.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    rect, frame = video_capture.read()    
    # Membalikkan frame secara horizontal
    frame = cv2.flip(frame, 1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)       

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()