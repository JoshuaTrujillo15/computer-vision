import cv2 as cv

cap = cv.VideoCapture(0)
ret, frame = cap.read()

haar_cascade = cv.CascadeClassifier('data_sets/haar_face.xml')

while ret:
    # operations on frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), thickness=2)

    # display frame
    cv.imshow('frame', frame)
    ret, frame = cap.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()