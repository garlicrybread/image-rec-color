import cv2
import numpy as np


def main():
	# lower_range_apple = np.array([169, 10, 100], dtype=np.uint8)
	# upper_range_apple = np.array([180, 255, 255], dtype=np.uint8)

	# Load the image for finding where the objects are
	# img = cv2.imread("circles.png", 1)
	# img = cv2.imread("ao.jpeg", 1)
	# img = cv2.imread("shoe-ab.jpeg", 1)
	# img = cv2.imread("sidesmile.jpeg", 1)
	# img = cv2.imread("strsmile.jpeg", 1)
	# img = cv2.imread("smile.jpeg", 1)
	img = cv2.imread("2ap.jpeg", 1)

	img=cv2.resize(img,(340,220))
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	# Find the red apple
	lower_range_apple = np.array([169, 10, 100], dtype=np.uint8)
	upper_range_apple = np.array([180, 255, 255], dtype=np.uint8)
	red = [30,30,200]
	center_of_apple = find_element_within_range(img, imgHSV, lower_range_apple, upper_range_apple,red)
	cv2.imshow('image', img)
	cv2.waitKey(0)


	# Find the orange
	lower_range_orange = np.array([0,200,250], dtype=np.uint8)
	upper_range_orange = np.array([100,255,255], dtype=np.uint8)
	orange = [40,127,255]
	center_of_orange = find_element_within_range(img, imgHSV, lower_range_orange, upper_range_orange, orange)
	cv2.imshow('image', img)
	cv2.waitKey(0)

	# Find the banana
	lower_range_banana = np.array([20,100,150], dtype=np.uint8)
	upper_range_banana = np.array([50,200,255], dtype=np.uint8)
	yellow = [0,240,255]
	center_of_orange = find_element_within_range(img, imgHSV, lower_range_banana, upper_range_banana, yellow)
	cv2.imshow('image', img)
	cv2.waitKey(0)
	return 0 


def find_element_within_range(image, imgHSV, lower_range, upper_range, color):
	mask = cv2.inRange(imgHSV, lower_range, upper_range)

	cv2.imshow('mask',mask)
	cv2.waitKey(0)
	 
	element = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
	mask = cv2.erode(mask,element, iterations=2)
	mask = cv2.dilate(mask,element,iterations=2)
	mask = cv2.erode(mask,element)

	contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	maximumArea = 0
	bestContour = None
	for contour in contours:
		currentArea = cv2.contourArea(contour)
		if currentArea > maximumArea:
			bestContour = contour
			maximumArea = currentArea
	#Create a bounding box around the biggest red object
	x,y,w,h = (0,0,0,0)

	if bestContour is not None:
		x,y,w,h = cv2.boundingRect(bestContour)
		cv2.rectangle(image, (x,y),(x+w,y+h), color, 3)

	if x != 0:
		cv2.circle(image,(x+w/2,y+h/2),3,3)
		center = (x+w/2,y+h/2)
	else: 
		center = 0 

	return center


main()