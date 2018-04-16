import numpy as np
import cv2 as cv

img = cv.imread('ro.jpg',0)

dst = cv.cornerHarris(img,2,3,0.04)
dst = cv.dilate(dst,None)

img[dst>0.000001*dst.max()] = [255]
dst[dst>0.000001*dst.max()] = [255]

cv.imshow('img',img)
cv.imshow('dst',dst)

cv.waitKey(0)
cv.destroyAllWindows()



print dst,np.shape(dst),dst.max()
