import cv2 as cv
import numpy as np

#IQ from Rainbow six siege
img = cv.imread("iq_sharp.png",0)

_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow("img",img)
cv.imshow("thres_bin",th2)

cv.waitKey(0)

cv.destroyAllWindows()