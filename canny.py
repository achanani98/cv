import numpy as np
import cv2 as cv

img = cv.imread('goku.jpg',0)

def nothing(x):
    pass

cv.namedWindow('edgy',cv.WINDOW_NORMAL)
cv.namedWindow('img',cv.WINDOW_NORMAL)
cv.createTrackbar('lower','edgy',100,255,nothing)
cv.createTrackbar('upper','edgy',200,255,nothing)

while(1):
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    lower = cv.getTrackbarPos('lower','edgy')
    upper = cv.getTrackbarPos('upper','edgy')
    edgy = cv.Canny(img,lower,upper)
    cv.imshow('img',img)
    cv.imshow('edgy',edgy)


cv.destroyAllWindows()
