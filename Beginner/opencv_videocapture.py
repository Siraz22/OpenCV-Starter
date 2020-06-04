import cv2

#0 - Use webcam in my case
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap.set(3,1)
cap.set(4,1)


print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
	

	ret, frame = cap.read()

	if(ret):
		
		out.write(frame)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('window_sample',gray)

		if(cv2.waitKey(1) == ord('q')):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()
