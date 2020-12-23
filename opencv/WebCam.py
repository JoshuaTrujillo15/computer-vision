import cv2 as cv

cv.namedWindow('preview')
vc = cv.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv.imshow('preview', frame)
    rval, frame = vc.read()
    key = cv.waitKey(20)
    if key == 27:
        break

cv.destroyWindow('preview')
vc.release()