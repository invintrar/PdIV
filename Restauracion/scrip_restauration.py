#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:33:35 2019

@author: Gustavo
"""




import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np
from skimage.util import random_noise
from skimage.restoration import wiener,unsupervised_wiener,richardson_lucy
import scipy.fftpack as fp
from scipy import signal


############# Using the inverse filter to restore a blurred image

I = cv2.imread(('../images/lena_gray_512.tif'),0)
gauss = random_noise(I, mode='gaussian', seed=None, clip=True)

#create a gaussian degradation function
H_kernel = np.outer(signal.gaussian(I.shape[0], 12), signal.gaussian(I.shape[1], 12))
I_freq = fp.fft2(I)
assert(I_freq.shape == H_kernel.shape)
Hkernel_freq = fp.fft2(fp.ifftshift(H_kernel))
G_degradation = I_freq*Hkernel_freq # by the Convolution theorem
G_image = fp.ifft2(G_degradation).real
G_image = 255 * G_image / np.max(G_image)


#apply bluring to an image using skimage directly
#blur_gaussiano=gaussian(I, sigma=20,mode ='nearest',truncate=2.0)


## restauration##### 
epsilon = 10**-6
I_rest=G_degradation/(epsilon+Hkernel_freq)
I_rest = fp.ifft2(I_rest).real
restaurate = cv2.normalize(I_rest.astype('uint8'), None, 0, 255, cv2.NORM_MINMAX)


plt.subplot(221), plt.imshow(I,cmap='gray'), plt.title('Origin')
plt.subplot(222), plt.imshow(gauss,cmap='gray'), plt.title('Gaussian Noise')
plt.subplot(223), plt.imshow(G_image,cmap='gray'), plt.title('Blurring')
plt.subplot(224), plt.imshow(restaurate,cmap='gray'), plt.title('Restauration')

plt.show()


######################################
# create the motion blur kernel
im = cv2.imread(('../images/lena_gray_512.tif'),0)
size = 95

# generating the kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
H_kernel = kernel_motion_blur / size
H_kernel = np.pad(H_kernel, (((im.shape[0]-size)//2,(im.shape[0]-size)//2+1), ((im.shape[1]-size)//2,(im.shape[1]-size)//2+1)))
output = cv2.filter2D(im, -1, H_kernel)
######


####
I_freq = fp.fft2(im)
assert(I_freq.shape == H_kernel.shape)
Hkernel_freq = fp.fft2(fp.ifftshift(H_kernel))
G_degradation = I_freq*Hkernel_freq # by the Convolution theorem
G_image = fp.ifft2(G_degradation).real
G_image = 255 * G_image / np.max(G_image)
###


epsilon = 10**-6

freq = fp.fft2(G_image)
freq_kernel = fp.fft2(fp.ifftshift(H_kernel))
freq_kernel = 1 / (epsilon + freq_kernel)

convolved = freq*freq_kernel
im_restored = fp.ifft2(convolved).real
im_restored = im_restored / np.max(im_restored)

plt.subplot(131), plt.imshow(im,cmap='gray'), plt.title('Origin')
plt.subplot(132), plt.imshow(G_image,cmap='gray'), plt.title('motion_blur')
plt.subplot(133), plt.imshow(im_restored,cmap='gray'), plt.title('Inverse restoration')

plt.show()

############       Wiener     #####################

# create the motion blur kernel
im = cv2.imread(('../images/lena_gray_512.tif'),0)
size = 5

# generating the kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size
H_kernel = np.pad(kernel_motion_blur, (((im.shape[0]-size)//2,(im.shape[0]-size)//2), ((im.shape[1]-size)//2,(im.shape[1]-size)//2)))
output = cv2.filter2D(im, -1, H_kernel)
Degradate_image= random_noise(output, mode='gaussian', seed=None, clip=True)
psf = kernel_motion_blur
deconvolved_img = wiener(Degradate_image, psf, 10)
deconvolvedW,_ = unsupervised_wiener(Degradate_image, psf)

plt.subplot(221), plt.imshow(im,cmap='gray'), plt.title('Origin')
plt.subplot(222), plt.imshow(Degradate_image,cmap='gray'), plt.title('G_image')
plt.subplot(223), plt.imshow(deconvolved_img,cmap='gray'), plt.title('Wiener')
plt.subplot(224), plt.imshow(deconvolvedW,cmap='gray'), plt.title('unsupervised_wiener')

plt.show()

######