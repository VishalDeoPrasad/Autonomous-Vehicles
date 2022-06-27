import cv2
import sys
import numpy as np

img = cv2.imread("car.png")
img = cv2.resize(img, (640, 480))

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

while True:
	h_min = cv2.getTrackbarPos("HUE Min", "HSV")
	h_max = cv2.getTrackbarPos("HUE Max", "HSV")

	s_min = cv2.getTrackbarPos("SAT Min", "HSV")
	s_max = cv2.getTrackbarPos("SAT Max", "HSV")

	v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
	v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(img, lower, upper)
	result = cv2.bitwise_and(img, img, mask = mask)

	cv2.imshow("result", result)
	cv2.waitKey(0)
cv2.destroyAllWindows()



