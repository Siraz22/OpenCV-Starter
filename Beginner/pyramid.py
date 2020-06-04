import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img = cv.imread("lena.jpg")

'''
lower_res = cv.pyrDown(img)
lr_2 = cv.pyrUp(lower_res)

cv.imshow("Orig",img)
cv.imshow("lower_res",lower_res)
cv.imshow("higher_res",lr_2)
'''

layer = img.copy()
gp = [layer]

for i in range(5):
	curr = cv.pyrDown(gp[-1])
	gp.append(curr)
	#cv.imshow(str(i),curr)

layer = gp[len(gp)-1]
cv.imshow("Upper level Gauss pyramid",layer)

lp = [layer]

for i in range(5,0,-1):
	extended = cv.pyrUp(gp[i])
	laplacian = cv.subtract(gp[i-1],extended)
	cv.imshow(str(i),laplacian)

cv.waitKey(0)
cv.destroyAllWindows()