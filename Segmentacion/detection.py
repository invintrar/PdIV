
import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage.segmentation as seg
from skimage.io import imread
import skimage.filters as filters
import skimage.restoration as resto
import skimage.draw as draw
import skimage.color as color
from skimage import exposure
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
from skimage.color import lab2rgb
import matplotlib.patches as mpatches

min = 73
max = 102

#Leemos la imagen
image = cv2.imread('toro.jpg',cv2.IMREAD_GRAYSCALE)
imag1 = image.copy()
img = image.copy()


# Calculamos el histograma
hist = cv2.calcHist([image], [0], None, [256], [0, 256])


#aplicamos filtros
med = filters.median(image)


# Thresholding using THRESH_TOZERO_OTSU
th6, dst6 = cv2.threshold(med, min, max,cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(dst6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(imag1, contours, -1, (200,0,0), 1)

#Clear objects connected to the label image border.
img_bin = clear_border(closing(imag1 > 120, square(20)))


#etiqueta los objetos
labels = label(img_bin)


plt.subplot(2,3,1)
plt.imshow(image,cmap='gray')
obj_ttl=plt.title('Original Image')
plt.setp(obj_ttl,color='b')
plt.axis("off")

plt.subplot(2,3,2)
plt.plot(hist, color='gray' )
obj_xl=plt.xlabel('Intensidad Iluminacion')
plt.setp(obj_xl,color='g')
obj_yl=plt.ylabel('Numero Pixeles')
plt.setp(obj_yl,color='g')
obj_ttl=plt.title("Histograma")
plt.setp(obj_ttl,color='b')

plt.subplot(2,3,3)
plt.imshow(dst6,cmap='gray')
obj_ttl=plt.title('THRESH_TOZERO_OTSU')
plt.setp(obj_ttl,color='b')
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(img_bin,cmap='gray')
obj_ttl=plt.title('Closing')
plt.setp(obj_ttl,color='b')
plt.axis("off")


plt.subplot(2,3,5)
plt.imshow(labels,cmap=plt.cm.rainbow)
obj_ttl=plt.title('Label')
plt.setp(obj_ttl,color='b')
plt.axis("off")


plt.subplot(2,3,6)
plt.imshow(imag1,cmap='gray')
obj_ttl=plt.title('Edge Otsu')
plt.setp(obj_ttl,color='b')
plt.axis("off")

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()



### usar las regiones
regions = regionprops(labels)
boxes = np.array([label['BoundingBox'] for label in regions if label['Area'] < 50])

print(f"There are {len(boxes)} objetos")

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.imshow(img, cmap=plt.cm.gray)
#ax.set_axis_off()

# Get the coordinates of the boxes.
xs = boxes[:, [1, 3]].mean(axis=1)
ys = boxes[:, [0, 2]].mean(axis=1)

# We reorder the boxes by increasing
# column first, and row second.
for row in range(4):
    # We select the coins in each of the four rows.
    if row < 3:
        ind = ((ys[6 * row] <= ys) &
               (ys < ys[6 * row + 6]))
    else:
        ind = (ys[6 * row] <= ys)
    # We reorder by increasing x coordinate.
    ind = np.nonzero(ind)[0]
    reordered = ind[np.argsort(xs[ind])]
    xs_row = xs[reordered]
    ys_row = ys[reordered]
    # We display the coin number.
    for col in range(6):
        n = 6 * row + col
        ax.text(xs_row[col] - 5, ys_row[col] + 5,
                str(n),
                fontsize=20)
        
        
#####plot bounding box############
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img,cmap=plt.cm.gray)
        
for region in regionprops(labels):
    # take regions with large enough areas
    if region.area >= 100:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


