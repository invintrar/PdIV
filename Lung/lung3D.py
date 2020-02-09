
import faux
import resampling
import ploting3D
import segmentacion
import displaySt

import numpy as np
import pydicom
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
# init_notebook_mode(connected=True)

# Pacientes id
id = 3
# Carpeta donde se almacenara los resultados
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"


#Funciones para graficar en 3D
grafica = np.load(output_path + "graficar_%d.npy" % (id))
v, f = ploting3D.make_mesh(grafica, 500)
#ploting3D.plt_3d(v, f)
ploting3D.plotly_3d(v,f)

