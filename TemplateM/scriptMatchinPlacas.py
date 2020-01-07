#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:50:33 2020

@author: Gustavo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


#path='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/Varios/placas/'


img_gray = cv2.imread('y02.jpg',1)
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


template = cv2.imread('template.png',1)
scale_percent = 100 # percent of original size
width = int(template.shape[1] * scale_percent / 100)
height = int(template.shape[0] * scale_percent / 100)
dim = (width,height)
Rtemplate = cv2.resize(template, dim, interpolation = cv2.INTER_AREA)
w, h = Rtemplate.shape[::-1]


res = cv2.matchTemplate(img_gray,Rtemplate,cv2.TM_CCOEFF_NORMED)
threshold = 0.3
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

plt.subplot(131),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(Rtemplate,cmap = 'gray')
plt.title('template'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_rgb)
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()