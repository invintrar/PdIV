"""
====================
Active Contour Model
====================

The active contour model is a method to fit open or closed splines to lines or
edges in an image [1]_. It works by minimising an energy that is in part
defined by the image and part by the spline's shape: length and smoothness. The
minimization is done implicitly in the shape energy and explicitly in the
image energy.

In the following two examples the active contour model is used (1) to segment
the face of a person from the rest of an image by fitting a closed curve
to the edges of the face and (2) to find the darkest curve between two fixed
points while obeying smoothness considerations. Typically it is a good idea to
smooth images a bit before analyzing, as done in the following examples.

We initialize a circle around the astronaut's face and use the default boundary
condition ``bc='periodic'`` to fit a closed curve. The default parameters
``w_line=0, w_edge=1`` will make the curve search towards edges, such as the
boundaries of the face.

.. [1] *Snakes: Active contour models*. Kass, M.; Witkin, A.; Terzopoulos, D.
       International Journal of Computer Vision 1 (4): 321 (1988).
       DOI:`10.1007/BF00133570`
"""

import numpy as np
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage import data
from skimage.segmentation import active_contour

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import cv2 
import sys
sys.path.insert(0, '/Users/Gustavo/AnacondaProjects/pythonCode/7_Librerias/segmentation/')
import curves as cuv
import segmentation as seg



path='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/Varios/'
pathVFmuscle='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/VFDATABASE/Crop1_muscle/'
pathVFcolageno='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/VFDATABASE/Crop6_collagane/'


refPt=[]
src = cv2.imread(path+"guineo.jpg");
srcshow = src.copy()
cv2.namedWindow('input')
cv2.imshow('input',srcshow)
cv2.setMouseCallback('input', seg.on_mouse,param=(srcshow,refPt))
cv2.waitKey()
cv2.destroyAllWindows()

xs=[refPt[i][1] for i in range(len(refPt))]
ys=[refPt[i][0] for i in range(len(refPt))]
poly = Polygon(list(zip(xs, ys)), animated=True)

fig, ax = plt.subplots(figsize=(7, 7))
ax.add_patch(poly)
p = cuv.PolygonInteractor(ax, poly, visible=False)
ax.set_title('Click and Fix the contour')
ax.imshow(src, cmap=plt.cm.gray)
plt.show()


x,y=p.interpolate()
init = np.array([x, y]).T
snake = active_contour(gaussian(src,3),init, alpha=0.015, beta=10, gamma=0.001)

ax.plot(snake[:, 0], snake[:, 1], '-r', lw=3)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, src.shape[1], src.shape[0], 0])

plt.show()

