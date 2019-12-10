import pydicom as dicom
import os
import PIL # optional
import pandas as pd
import numpy as np
import csv
# list of attributes available in dicom image
dicom_image_description = pd.read_csv('C:\\Users\\Darwin\\Documents\\GitHub\\Dsp\\ProyectoFinal\\DICOM-to-JPG\\dicom_image_description.csv')
path ='C:\\Users\\Darwin\\Documents\\GitHub\\Dsp\\ProyectoFinal\\DICOM-to-JPG\\Patient_Detail.csv'
#print(dicom_image_description)
# Specify the .dcm folder path
folder_path = 'C:\\Users\\Darwin\\Documents\\NSCLC-RADIOMICS-INTEROBSERVER1\\interobs05\\02-18-2019-CT-90318\\28629\\'

images_path = os.listdir(folder_path)

# Patient's information will be stored in working directory #'Patient_Detail.csv'
with open(path, 'w', newline ='') as csvfile:
    fieldnames = list(dicom_image_description["Description"])
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(fieldnames)
    for image in images_path:
        ds = dicom.dcmread(folder_path + image)
        rows = []
        for field in fieldnames:
            if ds.data_element(field) is None:
                rows.append('')
            else:
                x = str(ds.data_element(field)).replace("'", "")
                y = x.find(":")
                x = x[y+2:]
                rows.append(x)
        writer.writerow(rows)