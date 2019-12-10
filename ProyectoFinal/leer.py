import numpy as np
import cv2
import pydicom 
from pydicom.data import get_testdata_files

path = "C:\\Users\\Darwin\\Documents\\NSCLC-RADIOMICS-INTEROBSERVER1\\interobs05\\02-18-2019-CT-90318\\28629\\"
#filename = get_testdata_files("rtplan.dcm")[0]
ds = pydicom.read_file(path+"000004.dcm")  # plan dataset
#ConstPixwlDims = (int(ds.Rows), int(ds.Columns), len(lstFilesDCM))
dcm_sample=ds.pixel_array*128
cv2.imshow('sample image dicom',dcm_sample)
print(ds.PatientName)


cv2.waitKey()
cv2.destroyAllWindows()