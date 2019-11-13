#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:31:21 2019

@author: Gustavo
"""

# import opencv 
import cv2 
import matplotlib.pyplot as plt

path='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/Varios/'


# Read image 
src = cv2.imread(path+"lena.png", cv2.IMREAD_GRAYSCALE); 
cv2.imshow("original",src)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Basic threhold example 
th, dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY); 
cv2.imshow("images1",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-threshold-example.jpg", dst); 


# Thresholding with maxValue set to 128
th, dst = cv2.threshold(src, 127, 128, cv2.THRESH_BINARY); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-binary-maxval.jpg", dst); 



# Thresholding using THRESH_BINARY_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY_INV); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-binary-inv.jpg", dst); 

# Thresholding using THRESH_TRUNC 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TRUNC); 
cv2.imshow("images1",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-trunc.jpg", dst); 

# Thresholding using THRESH_TOZERO 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-tozero.jpg", dst); 

# Thresholding using THRESH_TOZERO_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO_INV); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-to-zero-inv.jpg", dst); 

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
ret,thr = cv2.threshold(src, 0, 255,cv2.THRESH_OTSU)
cv2.imshow("images",thr)
cv2.waitKey(0)
cv2.destroyAllWindows()


####GUINEO###
imgray = cv2.imread(path+"guineo.jpg");
cv2.imshow("guineo",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
b,g,r=cv2.split(imgray)
plt.hist(b.ravel(),256,[0,256]); plt.show()
cv2.imshow("Imagen",b)
cv2.waitKey(0)
cv2.destroyAllWindows()


####threslhold
ret, thresh2 = cv2.threshold(imgray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("threshold",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#To draw all the contours in an image:
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(imgray, contours, -1, (255,0,0), 3)
cv2.imshow("images",imgray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
##To draw an individual contour, say 4th contour:
#cv2.drawContours(imgray, contours, 3, (0,255,0), 3)
#cv2.imshow("images",imgray)
#cv2.waitKey(0)
##But most of the time, below method will be useful:
#cnt = contours[4]
#cv2.drawContours(imgray, [cnt], 0, (0,255,0), 3)




############OTSU###############################
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import coins
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
from skimage.color import lab2rgb
import matplotlib.patches as mpatches


### función para graficar imagen
def show(img, cmap=None):
    cmap = cmap or plt.cm.gray
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.imshow(img, cmap=cmap)
    ax.set_axis_off()
    plt.show()

#cargo iamgen coins
img = coins()
show(img)

##utilizo otsu para la segmentación
threshold_otsu(img)
show(img > 107)

#Clear objects connected to the label image border.
img_bin = clear_border(closing(img > 120, square(5)))
show(img_bin)

#etiqueta los objetos
labels = label(img_bin)
show(labels, cmap=plt.cm.rainbow)

### usar las regiones
regions = regionprops(labels)
boxes = np.array([label['BoundingBox'] for label in regions if label['Area'] > 100])
print(f"There are {len(boxes)} coins.")

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.imshow(img, cmap=plt.cm.gray)
ax.set_axis_off()

# Get the coordinates of the boxes.
xs = boxes[:, [1, 3]].mean(axis=1)
ys = boxes[:, [0, 2]].mean(axis=1)

# We reorder the boxes by increasing
# column first, and row second.
for row in range(4):
    # We select the coins in each of the four rows.
    if row < 3:
        ind = ((ys[6 * row] <= ys) &
               (ys < ys[6 * row + 6]))
    else:
        ind = (ys[6 * row] <= ys)
    # We reorder by increasing x coordinate.
    ind = np.nonzero(ind)[0]
    reordered = ind[np.argsort(xs[ind])]
    xs_row = xs[reordered]
    ys_row = ys[reordered]
    # We display the coin number.
    for col in range(6):
        n = 6 * row + col
        ax.text(xs_row[col] - 5, ys_row[col] + 5,
                str(n),
                fontsize=20)
        
        
#####plot bounding box############
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img,cmap=plt.cm.gray)
        
for region in regionprops(labels):
    # take regions with large enough areas
    if region.area >= 100:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()



















#### Histogram equalization
import cv2

equ = cv2.equalizeHist(src) 
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(src)



hist = cv2.calcHist([src],[0],None,[256],[0,256])

img = cv2.imread('home.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.show()
   
    
    
    