import numpy as np
import cv2 as cv

img = cv.imread("ro.jpg",1)
img = np.array(img)
# h,w = np.shape(img)

blur = cv.GaussianBlur(img,(11,11),0)
img1 = cv.Laplacian(img,cv.CV_64F)
# sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
# sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
# sobelxy = cv.Sobel(img,cv.CV_64F,1,1,ksize=7)


# for i in range(1,h-1):
#     img[i] = img[i+1]-img[i]
#
img2 = cv.Laplacian(blur,cv.CV_64F)
# print h,w
#
# img3 = cv.imread("ro.jpg",0)
# img3 = np.array(img3)
# h,w = np.shape(img3)
#
# for i in range(1,w-1):
#     img3[:,i] = img3[:,i+1]-img3[:,i]
#

cv.imshow('blur',blur)
# cv.imshow('sxy`',sobelxy)
#
# cv.imshow('sx',sobelx)
# cv.imshow('sy',sobely)
cv.imshow('img',img)
# cv.imshow('img3',img3[:][:-1])
cv.imshow('lp',img1)
cv.imshow('imgdxlp',img2)
cv.waitKey(0)
cv.destroyAllWindows()
