
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
import skimage.segmentation as seg
from skimage.io import imread

import skimage.filters as filters
import skimage.restoration as resto
import skimage.draw as draw
import skimage.color as color
from skimage import exposure

img = cv2.imread('toro.jpg',0)

cv2.imshow('Toro',img)


cv2.waitKey(0)
cv2.destroyAllWindows()