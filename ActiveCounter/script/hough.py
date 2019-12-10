#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:26:38 2019

@author: Gustavo
"""
import cv2
import numpy as np
import sys

path='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/Varios/'


def onTrackbarChange(max_slider):
	global img
	global dst
	global gray

	dst = np.copy(img)

	th1 = max_slider 
	th2 = th1 * 0.4
	edges = cv2.Canny(img, th1, th2)
	
	# Apply probabilistic hough line transform
	lines = cv2.HoughLinesP(edges, 2, np.pi/180.0, 50, minLineLength=80, maxLineGap=100)

	# Draw lines on the detected points
	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv2.line(dst, (x1, y1), (x2, y2), (0,0,255), 2)

	cv2.imshow("Result Image", dst)	
	cv2.imshow("Edges",edges)

if __name__ == "__main__":
	
	# Read image
	img = cv2.imread(path+'lines.jpg')
	
	# Create a copy for later usage
	dst = np.copy(img)

	# Convert image to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Create display windows
	cv2.namedWindow("Edges")
	cv2.namedWindow("Result Image")
	  

	# Initialize threshold value
	initThresh = 500

	# Maximum threshold value
	maxThresh = 1000

	cv2.createTrackbar("threshold", "Result Image", initThresh, maxThresh, onTrackbarChange)
	onTrackbarChange(initThresh)

	while True:
		key = cv2.waitKey(1)
		if key == 27:
			break

	cv2.destroyAllWindows()