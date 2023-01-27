import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([60,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    img = cv.imread(mask,0)
    ret,thresh = cv.threshold(img,127,255,0)
    contours,hierarchy = cv.findContours(thresh, 1, 2)

    cnt = contours[0]
    M = cv.moments(cnt)
    #print( M )

    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
    k = cv.waitKey(5) & 0xFF
    if k == 40:
        break
cv.destroyAllWindows()