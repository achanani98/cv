import numpy as np
import cv2 as cv
#
# img = cv.imread('ro.jpg',0)

cam = cv.VideoCapture(0)

def nothing(x):
    pass

cv.namedWindow('edgy',cv.WINDOW_NORMAL)
cv.namedWindow('img',cv.WINDOW_NORMAL)
cv.createTrackbar('lower','edgy',100,255,nothing)
cv.createTrackbar('upper','edgy',200,255,nothing)

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret :


        lower = cv.getTrackbarPos('lower','edgy')
        upper = cv.getTrackbarPos('upper','edgy')
        edgy = cv.Canny(frame,lower,upper)
        cv.imshow('img',frame)
        cv.imshow('edgy',edgy)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cv.destroyAllWindows()
