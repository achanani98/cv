import numpy as np
import cv2 as cv
cam = cv.VideoCapture(0)

while(cam.isOpened()):

    ret,frame = cam.read()
    if ret==True:
        frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.namedWindow('image', cv.WINDOW_NORMAL)
        #blur = cv.GaussianBlur(frame,(5,5),0)
        blur = cv.bilateralFilter(frame,9,75,75)
        edgy = cv.Laplacian(blur,cv.CV_64F)
        cv.imshow('frame',frame)
        cv.imshow('blur',blur)
        cv.imshow('edgy',edgy)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
cv.destroyAllWindows()
