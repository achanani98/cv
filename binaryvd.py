import numpy as np
import cv2 as cv
from copy import deepcopy
def nothing(x):
    pass

cv.namedWindow('frame')
cam = cv.VideoCapture(0)
T = cv.createTrackbar('tval','frame',100,255,nothing)
br = cv.createTrackbar('bright','frame',50,100,nothing)

while(cam.isOpened()):

    ret,frame = cam.read()
    if ret :

        frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        frame += (cv.getTrackbarPos('bright','frame')-50)
        cv.imshow('frame1',frame)
        t = cv.getTrackbarPos('tval','frame')
        frame[frame>t] = 255
        frame[frame<=t] = 0

        cv.imshow('frame',frame)



        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
cv.destroyAllWindows()
