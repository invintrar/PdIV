#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:42:07 2019

@author: Gustavo
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import numpy as np

###k-means segmentation###########
def obtenerI(img):
    img = img.copy();
    #img1 = cv2.imread("paisaje.png")
    #img=cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)

#Next, converts the MxNx3 image into a Kx3 matrix where K=MxN and each 
#row is now a vector in the 3-D space of RGB.
    vectorized = img.reshape((-1,3))

#We convert the unit8 values to float as it is a requirement of the k-means
#method of OpenCV.
    vectorized = np.float32(vectorized)

#Define criteria, number of clusters(K) and apply k-means()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 10
    attempts=10
    ret,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

# Now convert back into uint8.
    center = np.uint8(center)

#Next, we have to access the labels to regenerate the clustered image
    res = center[label.flatten()]
    result_image = res.reshape((img.shape))
    result_image1=cv2.cvtColor(result_image,cv2.COLOR_LAB2BGR)
    img1= cv2.cvtColor(img,cv2.COLOR_LAB2BGR)
    
    return [img1, result_image1]

