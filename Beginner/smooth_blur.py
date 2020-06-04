import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img = cv.imread("iq_sharp.png")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(25,25))

#More blur at the center and weight decreases as we go away from center
g_blur = cv.GaussianBlur(img,(25,25),0)

titles = ['img','2D Conv','blur','gaussianBlur']
images = [img,dst,blur,g_blur]

for i in range(len(images)):
	plt.subplot(2,2,i+1),plt.imshow(images[i])
	plt.xticks([]),plt.yticks([])
	plt.title(titles[i])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()