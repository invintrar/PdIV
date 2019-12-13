import numpy as np
import pydicom
from pydicom.data import get_testdata_files
import os
import matplotlib.pyplot as plt
from glob import glob
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.ndimage
from skimage import morphology
from skimage import measure
from skimage.transform import resize
from sklearn.cluster import KMeans
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *



filename = get_testdata_files("data.dcm")[0]
ds = pydicom.dcmread(filename)  # plan dataset
print(ds.PatientName)
print(ds.dir("setup"))    # get a list of tags with "setup" somewhere in the name
print(ds.PatientSetupSequence[0])
ds.PatientSetupSequence[0].PatientPosition = "HFP"
ds.save_as("rtplan2.dcm")