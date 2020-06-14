import cv2 as cv
import numpy as np

#img = cv.imread('smarties.png')
#imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('contour_test.avi',fourcc,20,(640,480))

while(cap.isOpened()):

	#ret,thresh = cv.threshold(imggray,127,255,0)
	ret,frame = cap.read()
	gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	ret2,thresh = cv.threshold(gray_frame,127,255,0)

	contours,heirarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
	
	cv.drawContours(frame,contours,-1,(0,255,0),2)

	if(ret):
		out.write(frame)

		cv.imshow("window_sample",frame)

		if(cv.waitKey(1)==27):
			break
	else:
		break

#print("no of contours",len(contours))

#cv.imshow("image",img)
#cv.imshow("Contour",imggray)

cap.release()
out.release()
cv.destroyAllWindows()