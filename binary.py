import numpy as np
import cv2 as cv
from copy import deepcopy

def nothing(x):
    pass

cv.namedWindow('img',cv.WINDOW_NORMAL)
T = cv.createTrackbar('tval','img',100,255,nothing)

img = cv.imread('goku.jpg',1)
while(1):
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    t = cv.getTrackbarPos('tval','img')
    img1 = deepcopy(img)
    img1[img1>t] = 255
    img1[img1<=t] = 0
    cv.imshow('img',img1)


cv.destroyAllWindows()
