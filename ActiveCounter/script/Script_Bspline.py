#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:33:15 2019

@author: Gustavo
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import cv2 
import sys
sys.path.insert(0, '/Users/Gustavo/AnacondaProjects/pythonCode/7_Librerias/segmentation/')
import curves as cuv
import segmentation as seg

    #theta = np.arange(0, 2*np.pi, 0.1)
    #r = 1.5

    #xs = r*np.cos(theta)
    #ys = r*np.sin(theta)
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

#xs = (921, 951, 993, 1035, 1065, 1045, 993, 945)
#ys = (1181, 1230, 1243, 1230, 1181, 1130, 1130, 1130)
xs=[refPt[i][1] for i in range(len(refPt))]
ys=[refPt[i][0] for i in range(len(refPt))]


poly = Polygon(list(zip(xs, ys)), animated=True)
fig, ax = plt.subplots()
ax.add_patch(poly)


p = cuv.PolygonInteractor(ax, poly, visible=False)

ax.set_title('Click and drag a point to move it')

ax.set_xlim((0,src.shape[0]))
ax.set_ylim((src.shape[1],0))

plt.show()