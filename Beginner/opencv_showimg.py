import cv2
import numpy as np

img = cv2.imread('lena.jpg')

img = cv2.line(img, (90,0),(1,255),(255,0,0),5)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()