import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.patches as mpatches
from skimage.filters import roberts, sobel
from skimage import data, img_as_float, io
from skimage.morphology import label, closing, square
from skimage.segmentation import (morphological_chan_vese,
                                  morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set)


def store_evolution_in(lst):
    """Returns a callback function to store the evolution of the level sets in
    the given list.
    """

    def _store(x):
        lst.append(np.copy(x))

    return _store


fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax = axes.flatten()


# Morphological GAC
src = cv2.imread("image/yo4.png",0)
#scr1 = src[:, :, 1]
image = img_as_float(src)
image = sobel(image)
image = img_as_float(image)
gimage = inverse_gaussian_gradient(image)

# Initial level set
init_ls = np.zeros(image.shape, dtype=np.int8)
init_ls[20:-20, 20:-20] = 1
# List with intermediate results for plotting the evolution
evolution = []
callback = store_evolution_in(evolution)
ls = morphological_geodesic_active_contour(gimage, 100, init_ls,
                                           smoothing=10, balloon=-1,
                                           threshold=0.97,
                                           iter_callback=callback)

#etiqueta los objetos
labels = label(ls)

ax[0].imshow(image, cmap="gray")
ax[0].set_axis_off()
ax[0].contour(ls, [0.5], colors='r')
ax[0].set_title("Morphological GAC segmentation", fontsize=12)

ax[1].imshow(ls, cmap="gray")
ax[1].set_axis_off()
contour = ax[1].contour(evolution[-1], [0.5], colors='r')
contour.collections[0].set_label("Iteration 100")
ax[1].legend(loc="upper right")
title = "Morphological GAC evolution"
ax[1].set_title(title, fontsize=12)

fig.tight_layout()

plt.imshow(labels,cmap=plt.cm.rainblow)
object_ttl = plt.title('Label')
plt.setp(object_ttl,color = 'b')
plt.axis("off")

plt.show()
