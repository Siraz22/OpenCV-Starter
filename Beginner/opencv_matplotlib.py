import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.jpg",-1)
cv.imshow("image",img)

conv_color = cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.imshow(conv_color)
#plt.xticks([]),plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()