import cv2
import numpy as np

img = cv2.imread("lena.jpg",1)

_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)

resized = cv2.resize(img,None, fx = 0.5, fy =0.5)
threshold_resized = cv2.resize(th1,None,fx = 0.5,fy=0.5)
threshold_resized2 = cv2.resize(th2,None,fx = 0.5,fy=0.5)
threshold_resized3 = cv2.resize(th3,None,fx = 0.5,fy = 0.5)
threshold_resized4 = cv2.resize(th4,None,fx = 0.5,fy = 0.5)

#cv2.imshow("Img",resized)
#cv2.imshow("threshold",threshold_resized)
#cv2.imshow("threshold2",threshold_resized2)
#cv2.imshow("threshold3",threshold_resized3)
cv2.imshow("threshold4",threshold_resized4)

cv2.waitKey(0)
cv2.destroyAllWindows()