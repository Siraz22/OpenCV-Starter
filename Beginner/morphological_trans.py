import numpy as np
import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread('smarties.png',0)
_,mask = cv.threshold(img,200,255,cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)
dialation = cv.dilate(mask,kernal,iterations = 4)
erossion = cv.erode(mask,kernal,iterations = 4)

#Erosion followed by dialation.
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)

#Dialation and then erosion.
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)

titles = ['image','mask','dialation','erosion','opening','closing']
images = [img,mask,dialation,erossion,opening,closing]
for i in range(len(images)):

	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()