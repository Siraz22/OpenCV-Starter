import numpy as np
import cv2
import math

cap = cv2.VideoCapture(0)

def nothing(x):
	pass

cv2.namedWindow("Tracking")

cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",27,255,nothing)
cv2.createTrackbar("LV","Tracking",69,255,nothing)

cv2.createTrackbar("UH","Tracking",38,255,nothing)
cv2.createTrackbar("US","Tracking",105,255,nothing)
cv2.createTrackbar("UV","Tracking",130,255,nothing)

cv2.createTrackbar("Thresh","Tracking",127,255,nothing)

while(cap.isOpened()):

    #Capture frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.rectangle(frame, (100,100), (300,300), 
                    color = (255,0,0), 
                    thickness=2)
    
    cropped_img = frame[100:300, 100:300]

    #FILTERS
    blur = cv2.GaussianBlur(cropped_img,(3,3),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_s = cv2.getTrackbarPos("LS","Tracking")
    l_v = cv2.getTrackbarPos("LV","Tracking")

    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")

    thresh_low = cv2.getTrackbarPos("Thresh","Tracking")

    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    #MORPHOLOGICAL
    kernel = np.ones((5,5))

    dialation = cv2.dilate(mask, kernel, iterations=1)
    erosion = cv2.erode(dialation, kernel, iterations=1)

    filtered = cv2.GaussianBlur(erosion, (3,3), 0)
    ret, thresh = cv2.threshold(filtered, thresh_low,255,0)

    cv2.imshow("Threshold", thresh)

    #FINDING CONTOUR
    contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #To account for when there is no hand in ROI
    try:
        contour = max(contours, key = lambda x : cv2.contourArea(x))

        #Create bouding rectangle
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(cropped_img, (x,y), (x+w,y+h), (0,0,255), 0)

        #Find convex hull
        hull = cv2.convexHull(contour)

        #Drawing the contours
        drawing = np.zeros(cropped_img.shape, np.uint8)
        cv2.drawContours(drawing, [contour], -1, (0,255,0), thickness=0)
        cv2.drawContours(drawing, [hull], -1, (0,255,0), thickness=0)

        #Convex Defects
        hull= cv2.convexHull(contour, returnPoints= False)
        defects = cv2.convexityDefects(contour, hull)

        defect_counts = 0

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
            
            #print(angle)

            if angle<=90:
                defect_counts +=1
                #print(defect_counts)
                cv2.circle(cropped_img, far, 1 , [0,255,0],-1)

            cv2.line(cropped_img, start,end, [0,255,0],2)

        #Print number using defects
        if defect_counts >= 0 and defect_counts <= 4 :
            cv2.putText(frame, str(defect_counts+1) ,(50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),2)
        else:
            pass
    except:
        pass

    #show req images
    cv2.imshow("Gesture", frame)
    all_image = np.hstack((drawing, cropped_img))
    cv2.imshow("Contours",all_image)

    if(cv2.waitKey(1) == 27): #Press Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
