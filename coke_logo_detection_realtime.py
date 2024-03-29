import cv2
from coke_logo_detection.definitions import MODEL_PATH
from colorthief import ColorThief

faceCascade = cv2.CascadeClassifier(MODEL_PATH)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.3,
                                         minNeighbors=20,
                                         minSize=(30, 30),  # (60, 20),
                                         flags=cv2.CASCADE_SCALE_IMAGE
                                         )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()