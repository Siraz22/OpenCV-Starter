import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

def nothing(x):
	pass

cv.namedWindow("Tracking")

cv.createTrackbar("LH","Tracking",0,255,nothing)
cv.createTrackbar("LS","Tracking",0,255,nothing)
cv.createTrackbar("LV","Tracking",0,255,nothing)

cv.createTrackbar("UH","Tracking",255,255,nothing)
cv.createTrackbar("US","Tracking",255,255,nothing)
cv.createTrackbar("UV","Tracking",255,255,nothing)

#Progression Ideas
'''
1) Using a mask on the hsv and drawing contours on the threshold of the mask will give good binary distinctions
for the contours

2) We can cancel out some unnecessary noisey countours we can apply a blur on the image to smoothen the sharpness
in the maskings

3) We can calculate area of each contour to determine wether it is to be considered or not
'''

while (cap.isOpened()):
	
	ret,frame = cap.read()
	blurred_frame = cv.GaussianBlur(frame,(5,5), 0)

	#hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	hsv = cv.cvtColor(blurred_frame,cv.COLOR_BGR2HSV)

	l_h = cv.getTrackbarPos("LH","Tracking")
	l_s = cv.getTrackbarPos("LS","Tracking")
	l_v = cv.getTrackbarPos("LV","Tracking")

	u_h = cv.getTrackbarPos("UH","Tracking")
	u_s = cv.getTrackbarPos("US","Tracking")
	u_v = cv.getTrackbarPos("UV","Tracking")

	lower_bound = np.array([l_h,l_s,l_v])
	upper_bound = np.array([u_h,u_s,u_v])

	mask = cv.inRange(hsv,lower_bound,upper_bound)

	#Contours on the mask using thresh
	#Thresh is what we will draw contours on and not the mask
	ret2,thresh_of_mask = cv.threshold(mask,0,255,0)

	contours,heirarchy = cv.findContours(thresh_of_mask,
										cv.RETR_TREE,
										cv.CHAIN_APPROX_NONE)

	#We found video capture
	if(ret):

		for contour in contours:
			area = cv.contourArea(contour)

			if(area>10000):
				print(area)

				#Draw on top of frame, not blurred frame
				cv.drawContours(frame,contours,-1,(0,255,0),1)

		cv.imshow("Sample",frame)
		cv.imshow("Mask",mask)


		if(cv.waitKey(1)==27):
			break
	else:
		break

cap.release()
cv.destroyAllWindows()