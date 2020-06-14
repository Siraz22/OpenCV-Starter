import cv2 as cv
import numpy as np

def nothing(x):
	pass

cv.namedWindow("Tracking")

cv.createTrackbar("LH","Tracking",137,255,nothing)
cv.createTrackbar("LS","Tracking",145,255,nothing)
cv.createTrackbar("LV","Tracking",157,255,nothing)

cv.createTrackbar("UH","Tracking",240,255,nothing)
cv.createTrackbar("US","Tracking",240,255,nothing)
cv.createTrackbar("UV","Tracking",235,255,nothing)

#Progression Ideas
'''
1) Using a mask on the hsv and drawing contours on the threshold of the mask will give good binary distinctions
for the contours

2) We can cancel out some unnecessary noisey countours we can apply a blur on the image to smoothen the sharpness
in the maskings

3) We can calculate area of each contour to determine wether it is to be considered or not

JOIN CONTOURS

1) The using of a convex hull was a disaster. Totally unoptimized and non-practical

2) Using dialation is better. Will have more dialation followed by small erosions.
'''

while (True):
	
	frame = cv.imread('gimp.jpg')

	dialation_kernal = np.ones((2,2), np.uint8)
	erosion_kernal = np.ones((2,2), np.uint8)
	closing_kernal = np.ones((2,2),np.uint8)

	blurred_frame = cv.GaussianBlur(frame,(25,25), 0)

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
	
	mask = cv.inRange(blurred_frame,lower_bound,upper_bound)
	mask = 255-mask
	
	#Contours on the mask using thresh
	#Thresh is what we will draw contours on and not the mask
	ret2,thresh_of_mask = cv.threshold(mask,0,255,0)
	
	dialated_thresh = cv.dilate(thresh_of_mask,dialation_kernal,iterations = 25)
	eroded_thresh = cv.erode(dialated_thresh,erosion_kernal,iterations = 21)
	#closing = cv.morphologyEx(thresh_of_mask,cv.MORPH_CLOSE,dialation_kernal,iterations = 0)

	contours,heirarchy = cv.findContours(mask,
										cv.RETR_TREE,
										cv.CHAIN_APPROX_NONE)

	#We found valid image capture
	if(len(frame)!=0):
		for contour in contours:
			area = cv.contourArea(contour)

			if(area>100):
				#print(area)

				#Draw on top of frame, not blurred frame
				cv.drawContours(frame,contours,-1,(255,0,0),1,offset = (0,0)) 

				#offset = -ve of iterations of erosion

		frame_resized = cv.resize(frame,None,fx = 1,fy=1)
		mask_resized = cv.resize(mask,None,fx = 1,fy = 1)
		#dialated_thresh_resized = cv.resize(dialated_thresh,None,fx = 0.2,fy = 0.2)
		#eroded_thresh_resized = cv.resize(eroded_thresh,None,fx = 0.2,fy = 0.2)
		#closing_resized = cv.resize(closing,None,fx = 0.2,fy=0.2)
		
		cv.imshow("Sample",frame_resized)
		cv.imshow("Orig Mask",mask_resized)
		#cv.imshow("Dialated Mask",dialated_thresh_resized)
		#cv.imshow("Erosion of Dialated mask",eroded_thresh_resized)
		#cv.imshow("Closing of thresh_mask",closing_resized)

		if(cv.waitKey(1)==27):
			break
	else:
		break

cv.destroyAllWindows()