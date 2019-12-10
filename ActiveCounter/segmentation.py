#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:08:18 2019

@author: Gustavo
"""
import sys
import numpy as np
import cv2 

# Owner modules
sys.path.insert(0, '/Users/Gustavo/AnacondaProjects/pythonCode/7_Librerias/VocalFolds_module')
import VFmodule as vf


def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('Start Mouse Position: ' + str(x) + ', ' + str(y))
        point= (x, y)
        cv2.circle(param[0],point, 2, (2555, 0, 0), -1)
        cv2.imshow('input',param[0])
        param[1].append((y,x)) 
                         
     
def region_growing(img, seed):
    #Parameters for region growing
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    region_threshold = 0.2
    region_size = 1
    intensity_difference = 0
    neighbor_points_list = []
    neighbor_intensity_list = []
    region_mean=[]

    for j in range(len(seed)):
    #Mean of the segmented region
        region_mean.append(img[seed[j]])

        #Input image parameters
        height, width = img.shape
        image_size = height * width

        #Initialize segmented output image
        segmented_img = np.zeros((height, width, 1), np.uint8)

        #Region growing until intensity difference becomes greater than certain threshold
        while (intensity_difference < region_threshold) & (region_size < image_size):
            #Loop through neighbor pixels
            for i in range(4):
                #Compute the neighbor pixel position
                x_new = seed[j][0] + neighbors[i][0]
                y_new = seed[j][1] + neighbors[i][1]

                #Boundary Condition - check if the coordinates are inside the image
                check_inside = (x_new >= 0) & (y_new >= 0) & (x_new < height) & (y_new < width)

                #Add neighbor if inside and not already in segmented_img
                if check_inside:
                    if segmented_img[x_new, y_new] == 0:
                        neighbor_points_list.append([x_new, y_new])
                        neighbor_intensity_list.append(img[x_new, y_new])
                        segmented_img[x_new, y_new] = 255

            #Add pixel with intensity nearest to the mean to the region
            distance = abs(neighbor_intensity_list-region_mean[j])
            pixel_distance = min(distance)
            index = np.where(distance == pixel_distance)[0][0]
            segmented_img[seed[j][0], seed[j][1]] = 255
            region_size += 1

            #New region mean
            region_mean[j] = (region_mean*region_size + neighbor_intensity_list[index])/(region_size+1)
            if len(region_mean[j])>1:
                region_mean[j]=region_mean[j][0]
            #Update the seed value
            seed[j] = neighbor_points_list[index]
            #Remove the value from the neighborhood lists
            neighbor_intensity_list[index] = neighbor_intensity_list[-1]
            neighbor_points_list[index] = neighbor_points_list[-1]

    return segmented_img

#Kass, M.; Witkin, A.; Terzopoulos, D. “Snakes: Active contour models”.
#International Journal of Computer Vision 1 (4): 321 (1988). DOI:10.1007/BF00133570
#opt=[alpha,beta,w_line,w_edge,gamma,coordinates,boundary_condition]
#def active_contourKass(img3D,opt=[0.1,1.0,-5,0,0.1,'rc','fixed']):
#        ROI, imCrop2D = vf.manualROI(img3D,plot=False)
#        snake = active_contour(gaussian(img, 3),init, alpha=0.015, beta=10, gamma=0.001,
#                       coordinates='rc')
    




