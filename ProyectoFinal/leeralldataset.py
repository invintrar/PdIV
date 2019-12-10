import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt
import sys
import cv2

path = "C:\\Users\\Darwin\\Documents\\NSCLC-RADIOMICS-INTEROBSERVER1\\interobs05\\02-18-2019-CT-90318\\28629\\"

contar = 0

while valor :
    # specify your image path
    if(contar < 10):
        image_path = path + '00000' + str(contar) +'.dcm'
    #end
    if (contar >= 10 and valor < 100):
        image_path = path + '0000' + str(contar) +'.dcm'
    #end
    if (contar >= 100):
        image_path = path + '000' + str(contar) +'.dcm'
    #end
        
    ds = dicom.dcmread(image_path)
        
    plt.imshow( ds.pixel_array)
    plt.title(str(contar))
        
    plt.pause(0.01)
        
    contar += 1
    
plt.close()
        