import cv2
import sys
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
#cap.set(3, frameWidth)
#cap.set(4,frameHeight)

if cap.isOpened() == False:
	print("Problem with webcam!!")
	sys.exit()

def empty(a):
	pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

frame_counter = 0
while True:
	_, img = cap.read()
	img = cv2.resize(img, (640, 480))
	#infinite time video play
	frame_counter += 1
	#If the last frame is reached, reset the capture and the frame_counter
	if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
		frame_counter = 0 #Or whatever as long as it is the same as next line
		cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	h_min = cv2.getTrackbarPos("HUE Min", "HSV")
	h_max = cv2.getTrackbarPos("HUE Max", "HSV")
	
	s_min = cv2.getTrackbarPos("SAT Min", "HSV")
	s_max = cv2.getTrackbarPos("SAT Max", "HSV")

	v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
	v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

	print("HUE Range = ",h_min,h_max, "SAT Range = ", s_min, s_max, "Value Range = ", v_min, v_max)

	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(imgHSV, lower, upper)
	result = cv2.bitwise_and(img, img, mask = mask)

	mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
	hstack = np.hstack([img, mask, result])
	

	cv2.imshow("Horizontal Stacking", hstack)
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()

