import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img = cv.imread("sudoku.png",0)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

lap = cv.Laplacian(img,cv.CV_64F,ksize = 3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img,cv.CV_64F,1,0)
sobelY = cv.Sobel(img,cv.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#sobelCombine = cv.bitwise_or(sobelX,sobelY)

titles = ['img','Laplacian','SobelX','SobelY']
images = [img,lap,sobelX,sobelY]

for i in range(len(images)):
	plt.subplot(2,3,i+1),plt.imshow(images[i])
	plt.xticks([]),plt.yticks([])
	plt.title(titles[i])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()