import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img = cv.imread("sudoku.png",0)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

canny = cv.Canny(img,122,255)

titles = ['img',"canny_edges"]
images = [img,canny]

for i in range(len(images)):
	plt.subplot(1,2,i+1),plt.imshow(images[i])
	plt.xticks([]),plt.yticks([])
	plt.title(titles[i])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()