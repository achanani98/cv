import numpy as np
import cv2 as cv
from copy import deepcopy
import time

cv.namedWindow('img',flags = cv.WINDOW_NORMAL)
t = 0
img = cv.imread('ro.jpg',1)
img = cv.resize(img,(1080,720))
h,w,_ = img.shape


fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('outspecial.avi',fourcc, 20.0, (w,h))



while(t<70):
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    img1 = deepcopy(img)
    img1[img1>t],img1[img1<=t] = 255,0
    cv.imshow('img',img1)
    out.write(img1)
    t+=1
    time.sleep(0.05)

out.release()
cv.destroyAllWindows()
