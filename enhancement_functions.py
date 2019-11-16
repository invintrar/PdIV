#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:03:00 2019

@author: Gustavo
"""



import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from skimage.exposure import rescale_intensity


#### negative transformation for gray images#################
def Negative_transformation(image,option=1):
    if option==1:
        negative_image=255-image
    else:
        negative_image=cv2.bitwise_not(image)
    return negative_image
######################################################################
            
#### logaritmic transformation for gray images#################
def log_transformation(image, K=1.0):
    logImage=np.uint8(K*np.log1p(image))
    normalized_image = cv2.normalize(logImage, None, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
    return normalized_image
######################################################################





#### plot logaritmic #################
def log_plotTransformation(k,interval=np.linspace(0,256,500)):
    logImage=np.uint8(k*np.log1p(interval))
    spline_logImage = make_interp_spline(interval,logImage) #BSpline object
    log_smoothY = spline_logImage(interval)
    plt.plot(interval, log_smoothY)
    plt.show()
######################################################################




    
## Function that plot the histogram of gray image and the CDF
def plotHistogram_CDF(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum() 
    cdf_normalized = cdf * (hist.max()/ cdf.max())
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.title('CDF')
    plt.plot(cdf_normalized, '-b',linewidth=2)
    plt.xlabel("Levels")
    plt.ylabel("# pixels")
    plt.xlim([0,256])
    
    plt.subplot(2,1,2)
    plt.title('Histogram')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlabel("Levels")
    plt.ylabel("# pixels")
    plt.xlim([0,256])
    
    plt.subplots_adjust(hspace=0.5)
    plt.show()    
####################################################################################
    
    
    
    
## plot  the Transformation function used in image equalization
def PlotHistogramEQ_transformation(image):
    hist,bins = np.histogram(image.flatten(),256,[0,256])
    trans=np.zeros(np.size(hist))
    for i in range(256):
        trans[i]=(255/image.size)*sum(hist[:i])
    plt.figure()
    plt.title('Transformation')
    plt.plot(trans,'-b',linewidth=2)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.xlim([0,256])
    return trans,hist
####################################################################################

    
    
## Compute two version of image equalization and plot CDF and histogram
def Histogram_Equalization(img,option=1,plot=0):
    histOrig,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = histOrig.cumsum()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img_eq = cdf[img]
    histEQ,bins = np.histogram(img_eq.flatten(),256,[0,256])
    cdfEQ = histEQ.cumsum()
    cdf_normalizedEQ = cdfEQ * (histEQ.max()/ cdfEQ.max())
    
    if option != 1:
        img_eq = cv2.equalizeHist(img)
        
    if plot==1:
        plt.figure()
        plt.subplot(2,1,1)
        plt.title('CDF')
        plt.plot(cdf_normalizedEQ, '-b',linewidth=2)
        plt.xlabel("Levels")
        plt.ylabel("# pixels")
        plt.xlim([0,256])
        
        plt.subplot(2,1,2)
        plt.title('Histogram')
        plt.hist(img_eq.flatten(),256,[0,256], color = 'r')
        plt.xlabel("Levels")
        plt.ylabel("# pixels")
        plt.xlim([0,256])
 
        plt.subplots_adjust(hspace=0.5)
        plt.show() 
    
    return img_eq
####################################################################################



## Compute  image equalization and plot CDF and histogram
def histeqV2(im,nbr_bins=256,plot=0):

   #get image histogram
   imhist,bins = np.histogram(im.flatten(),nbr_bins,normed=True)
   cdf = imhist.cumsum() #cumulative distribution function
   cdf = 255 * cdf / cdf[-1] #normalize

   #use linear interpolation of cdf to find new pixel values
   im2 = np.interp(im.flatten(),bins[:-1],cdf)#mapping function
   
   histEQ,bins = np.histogram(im2.flatten(),256,[0,256])
   cdfEQ = histEQ.cumsum()
   cdf_normalizedEQ = cdfEQ * (histEQ.max()/ cdfEQ.max())
   
   if plot==1:
       plt.figure()
       plt.subplot(2,1,1)
       plt.title('CDF Equalized')
       plt.plot(cdf_normalizedEQ, '-b',linewidth=2)
       plt.xlabel("Levels")
       plt.ylabel("# pixels")
       plt.xlim([0,256])
        
       plt.subplot(2,1,2)
       plt.title('Histogram Equalize')
       plt.hist(im2.flatten(),256,[0,256], color = 'r')
       plt.xlabel("Levels")
       plt.ylabel("# pixels")            
       plt.xlim([0,256])
 
       plt.subplots_adjust(hspace=0.5)
       plt.show() 

   return im2.reshape(im.shape), cdf
####################################################################################





### Histogram matching, give a Image target to create the matching
def HistogramMatching(imsrc,imtarget,nbr_bins=255,plot=0):

    if len(imsrc.shape) < 3:
        imsrc = imsrc[:,:,np.newaxis]
        imtarget  = imtarget[:,:,np.newaxis]

    imres = imsrc.copy()
    for d in range(imsrc.shape[2]):
        imhist,bins = np.histogram(imsrc[:,:,d].flatten(),nbr_bins,normed=True)
        tinthist,bins = np.histogram(imtarget[:,:,d].flatten(),nbr_bins,normed=True)

        cdfsrc = imhist.cumsum() #cumulative distribution function
        cdfsrc = (255 * cdfsrc / cdfsrc[-1]).astype(np.uint8) #normalize

        cdftint = tinthist.cumsum() #cumulative distribution function
        cdftint = (255 * cdftint / cdftint[-1]).astype(np.uint8) #normalize

        im2 = np.interp(imsrc[:,:,d].flatten(),bins[:-1],cdfsrc)
        im3 = np.interp(im2,cdftint, bins[:-1])
        imres[:,:,d] = im3.reshape((imsrc.shape[0],imsrc.shape[1] ))
    
    if plot==1:
        cv2.imshow('Original',imsrc.astype('uint8'))
        cv2.imshow('Histogram Matching',imres.astype('uint8'))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
           
        plt.figure()
        plt.subplot(2,1,1)
        plt.title('CDF')
        plt.plot(cdftint, '-b',linewidth=2)
        plt.xlabel("Levels")
        plt.ylabel("# pixels")
        plt.xlim([0,256])
        
        plt.subplot(2,1,2)
        plt.title('Histogram Equalize')
        plt.hist(imres.flatten(),256,[0,256], color = 'r')
        plt.xlabel("Levels")
        plt.ylabel("# pixels")            
        plt.xlim([0,256])
 
        plt.subplots_adjust(hspace=0.5)
        plt.show() 

    return imres
####################################################################################





## CLAHE (Contrast Limited Adaptive Histogram Equalization)
def ContrastAdaptHistogramEqualization(image,clip_limit=3,tileGridSize=(8,8)):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tileGridSize)
    
    if image.shape[-1]==3:
        # convert image to LAB color model
        image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        # split the image into L, A, and B channels
        l_channel, a_channel, b_channel = cv2.split(image_lab)
        # apply CLAHE to lightness channel
        cl = clahe.apply(l_channel)
        # merge the CLAHE enhanced L channel with the original A and B channel
        merged_channels = cv2.merge((cl, a_channel, b_channel))
        # convert iamge from LAB color model back to RGB color model
        final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
    else:
        final_image = clahe.apply(image)
    return final_image
####################################################################################



    
#### use skimage to make enhancement #####
##  https://scikit-image.org/docs/dev/api/skimage.exposure.html
    
## sharpeing filter there are two options to do it
def Sharpening(img,Kernelopt=1,option=1):
    if option:
        if Kernelopt:
            kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
        else:
            kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
        laplacian=cv2.filter2D(img,cv2.CV_64F,kernel)
        laplacian=rescale_intensity(laplacian, out_range=(0, 255))
        laplacian = laplacian.astype(np.uint8)
        return (img-0.7*laplacian)
    else:
        gaussian_3 = cv2.GaussianBlur(img, (9,9), 15.0)
        return(cv2.addWeighted(img, 1, gaussian_3, -0.5, 0, img))
####################################################################################

     
        
        