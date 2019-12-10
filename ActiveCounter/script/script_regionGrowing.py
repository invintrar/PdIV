#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:29:13 2019

@author: Gustavo
"""

import cv2 
#from skimage.io import imread
from matplotlib import pyplot as plt

import sys
# Owner modules
sys.path.insert(0, '/Users/Gustavo/AnacondaProjects/pythonCode/7_Librerias/segmentation/')
import segmentation as seg




path='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/Varios/'
pathVFmuscle='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/VFDATABASE/Crop1_muscle/'
pathVFcolageno='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/VFDATABASE/Crop6_collagane/'



refPt=[]
#ImgVFmuscle0=imread(pathVFmuscle+'0000.tif',as_gray='True')
src = cv2.imread(path+"mula.jpg");
srcshow = src.copy()
cv2.namedWindow('input')
cv2.imshow('input',srcshow)
cv2.setMouseCallback('input', seg.on_mouse,param=(srcshow,refPt))
cv2.waitKey()
print ("Starting region growing based on last click")
seed = refPt
src_gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
RGimg=seg.region_growing(src_gray, seed)
RG_smooth = cv2.GaussianBlur(RGimg, (3, 3), 0)
OverMask = cv2.bitwise_and(src, src, mask = RG_smooth)
    
fig, axes = plt.subplots(nrows=1,ncols=3, sharex=True, sharey=True,
                       figsize=(12, 4))
ax = axes.ravel()

ax[0].imshow(srcshow)
ax[0].set_title('Original Image')

ax[1].imshow(RG_smooth, cmap=plt.cm.gray)
ax[1].set_title('Region Growing segmentation')

ax[2].imshow(OverMask)
ax[2].set_title('Overlapping')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()   


