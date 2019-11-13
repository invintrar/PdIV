import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib

from skimage import data

matplotlib.rcParams['font.size'] = 18

fig, axes = plt.subplots(1, 2, figsize = (8, 4))
ax = axes.ravel()

images = data.stereo_motorcycle()
ax[0].imshow(images[0])
ax[1].imshow(images[2])

fig.tight_layout()
plt.show()