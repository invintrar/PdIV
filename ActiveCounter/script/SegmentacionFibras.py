#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:44:03 2019

@author: Gustavo
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
import skimage.segmentation as seg

import skimage.filters as filters
import skimage.restoration as resto
import skimage.draw as draw
import skimage.color as color
from skimage.external.tifffile import imread
from skimage import exposure


#import enhancement_functions as enh
#import signal_function as sig


pathVFmuscle='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/VFDATABASE/Crop1_muscle/'
pathVFcolageno='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/VFDATABASE/Crop6_collagane/'


ImgVFmuscle0=imread(pathVFmuscle+'0000.tif')
ImgVFmuscle1=imread(pathVFmuscle+'0001.tif')
ImgVFcolageno0=imread(pathVFcolageno+'Image_0000.tif')
ImgVFcolageno1=imread(pathVFcolageno+'Image_0001.tif')

plt.subplot(2,2,1),plt.imshow(ImgVFmuscle0,cmap='viridis')
plt.subplot(2,2,2),plt.imshow(ImgVFmuscle1,cmap='gray')
plt.subplot(2,2,3),plt.imshow(ImgVFcolageno0,cmap='gray')
plt.subplot(2,2,4),plt.imshow(ImgVFcolageno1,cmap='gray')


edge_sobel = filters.sobel(ImgVFmuscle0)
edge_prewit= filters.prewitt(ImgVFmuscle0)
edge_prewitt_v=filters.prewitt_v(ImgVFmuscle0)
edge_prewitt_h=filters.prewitt_h(ImgVFmuscle0)

fig, axes = plt.subplots(nrows=2,ncols=3, sharex=True, sharey=True,
                       figsize=(8, 8))
ax = axes.ravel()

ax[0].imshow(ImgVFmuscle0, cmap=plt.cm.gray)
ax[0].set_title('Original Image')

ax[1].imshow(edge_sobel, cmap=plt.cm.gray)
ax[1].set_title('Roberts Edge Detection')

ax[2].imshow(edge_prewit, cmap=plt.cm.gray)
ax[2].set_title('Prewit Edge Detection')

ax[3].imshow(edge_prewitt_v, cmap=plt.cm.gray)
ax[3].set_title('Prewit vertical Edge Detection')

ax[4].imshow(edge_prewitt_h, cmap=plt.cm.gray)
ax[4].set_title('Prewit Horizontal Edge Detection')

ax[5].imshow(angle(edge_prewitt_h, edge_prewitt_v), cmap=plt.cm.hsv)
ax[5].set_title('Sobel Edge Detection')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()

####### bordes musculo#############

#### CLAHE ##################
img_adapteq = exposure.equalize_adapthist(ImgVFmuscle0, clip_limit=0.03)
img_adapteq=resto.denoise_tv_chambolle(img_adapteq, weight=0.3, multichannel=True)

edge_roberts = filters.roberts(img_adapteq)
edge_sobel = filters.sobel(img_adapteq)

# Contrast stretching
p2, p98 = np.percentile(ImgVFmuscle0, (2, 98))
img_rescale = exposure.rescale_intensity(ImgVFmuscle0, in_range=(p2, p98))
img_rescale=resto.denoise_wavelet(img_rescale, sigma=0.3)
edge_robertsCS = filters.roberts(img_rescale)
edge_sobelCS = filters.sobel(img_rescale)



fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True,
                       figsize=(8, 4))

ax = axes.ravel()

ax[0].imshow(img_adapteq, cmap=plt.cm.gray)
ax[0].set_title('Clahe')

ax[1].imshow(edge_roberts, cmap=plt.cm.gray)
ax[1].set_title('Roberts Edge Detection')

ax[2].imshow(edge_sobel, cmap=plt.cm.gray)
ax[2].set_title('Sobel Edge Detection')

ax[3].imshow(img_adapteq, cmap=plt.cm.gray)
ax[3].set_title('img_rescale')

ax[4].imshow(edge_robertsCS, cmap=plt.cm.gray)
ax[4].set_title('Roberts Edge Detection')

ax[5].imshow(edge_sobelCS, cmap=plt.cm.gray)
ax[5].set_title('Sobel Edge Detection')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()




###############################

import skimage.io as skio
import skimage.filters as skfilt
import skimage.morphology as skmorph
import scipy.ndimage as ndi
from skimage.feature import peak_local_max

imstack1 = skio.imread(pathVFmuscle+'0000.tif', plugin="tifffile")
thresh_val = skfilt.threshold_otsu(imstack1)
new_mask = imstack1 > thresh_val
plt.imshow(new_mask,cmap='gray')

img_adapteq = exposure.equalize_adapthist(imstack1, clip_limit=0.03)

# First generate a distance transformed image 
dist = ndi.distance_transform_edt(img_adapteq)

# Next generate "markers": regions we are sure belong to different objects
local_maxi = peak_local_max(dist, indices=False, footprint=np.ones((3, 3)),labels=new_mask)
markers = ndi.label(local_maxi)[0]

# Lastly call the watershed transform - it takes the distance transform 
# and the markers as inputs (plus optionally the new_mask to delineate objects
# from background)
new_labels = skmorph.watershed(-dist, markers, mask=new_mask) 
plt.imshow(img_adapteq,cmap='gray')
plt.imshow(new_labels,cmap=plt.cm.nipy_spectral)


########################################
from skimage import exposure
from skimage import feature
from skimage.restoration import denoise_wavelet
from skimage.util import img_as_ubyte


def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged



image=ImgVFmuscle0.copy()
image.dtype, image.min(), image.max(), image.shape


out = exposure.rescale_intensity(image,out_range=(0,255))
out_ui8=img_as_ubyte(out)

edge_sobel = filters.sobel(out_ui8)
blurred = denoise_wavelet(out_ui8, sigma=0.1,  method='BayesShrink', mode='soft')
edge_canny = feature.canny(blurred, sigma=2)
#edges = auto_canny(blurred)
plt.imshow(edge_canny,cmap=plt.cm.gray)
plt.imshow(blurred,cmap=plt.cm.gray)










