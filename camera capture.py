import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()

	#Our operations on the frame ocme here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	#When all done release capture
	cap.release()
	#cv2.destroyAllWindows()