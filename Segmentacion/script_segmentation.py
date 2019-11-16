
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
import skimage.segmentation as seg
from skimage.io import imread

import skimage.filters as filters
import skimage.restoration as resto
import skimage.draw as draw
import skimage.color as color
from skimage import exposure


#import enhancement_functions as enh
#import signal_function as sig


ImgVFmuscle0=imread('toro.jpg',as_gray='True')
ImgVFmuscle1=imread('toro.jpg',as_gray='True')
ImgVFcolageno0=imread('toro.jpg',as_gray='True')
ImgVFcolageno1=imread('toro.jpg',as_gray='True')

plt.subplot(2,2,1),plt.imshow(ImgVFmuscle0,cmap='gray')
plt.subplot(2,2,2),plt.imshow(ImgVFmuscle1,cmap='gray')
plt.subplot(2,2,3),plt.imshow(ImgVFcolageno0,cmap='gray')
plt.subplot(2,2,4),plt.imshow(ImgVFcolageno1,cmap='gray')

'''
def angle(dx, dy):
    return np.arctan2(dy, dx)


########## bordes camera man###############
from skimage.data import camera
image = camera()
edge_sobel = filters.sobel(image)
edge_prewit= filters.prewitt(image)
edge_prewitt_v=filters.prewitt_v(image)
edge_prewitt_h=filters.prewitt_h(image)

fig, axes = plt.subplots(nrows=2,ncols=3, sharex=True, sharey=True,
                       figsize=(8, 8))
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
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
'''
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
