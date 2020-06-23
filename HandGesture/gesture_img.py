import cv2
import numpy as np

hand = cv2.imread("hand.jpg",0)

ret, thresh = cv2.threshold(hand, 70, 255, cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(contour) for contour in contours]
final = cv2.drawContours(hand, hull, -1, (255,0,255), thickness=2)

cv2.imshow("Thresh OP", thresh)
cv2.imshow("Sample Image",hand)
cv2.imshow("ConvexHUll", final)

cv2.waitKey(0)
cv2.destroyAllWindows()