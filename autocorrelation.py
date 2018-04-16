import numpy as np
import cv2 as cv
import copy

img = cv.imread('ro.jpg',0)

h,w = np.shape(img)
kernel = copy.deepcopy(img[h/4+10:h/4+20,w/4:w/4+10])

print kernel

correl = []
temp = 0
for i in range(h-10):
    tmp = []
    for j in range(w-10):
        E = 0
        for x in range(10):
            for y in range(10):
                yo = int(((int(img[i+x][j+y])-int(kernel[x][y]))**2))

                E += yo
                if (yo>=temp):
                    temp = yo

        tmp.append(int(E))
    correl.append(tmp)


correl  = np.array(correl)
hc,wc = np.shape(correl)


correl = (correl *255)/temp


cv.imshow('correl',correl)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
