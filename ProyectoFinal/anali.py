import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import dicom as pdicom
import os
import glob

%matplotlib inline

import pandas as pd 
import scipy.ndimage
from skimage import measure, morphology
from mpl_toolkits.mpl_toolkits.mplot3d.art3d import Poly3DCollection
