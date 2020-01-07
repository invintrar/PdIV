import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt
import sys
import cv2

path = "C:\\Users\\Darwin\\Documents\\NSCLC-RADIOMICS-INTEROBSERVER1\\interobs05\\02-18-2019-CT-90318\\28629\\"


image_path = path + '000000' +'.dcm'

ds = dicom.dcmread(image_path)

plt.imshow( ds.pixel_array)


plt.show()

plt.close()

