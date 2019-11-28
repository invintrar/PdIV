import cv2 
import matplotlib.pyplot as plt
import skimage.filters as filters

'''
min = 65
max = 115
# Read image 
src = cv2.imread("toro.jpg", cv2.IMREAD_GRAYSCALE); 

# THRESH_BINARY
th1, dst1 = cv2.threshold(src, min, max, cv2.THRESH_BINARY); 

# Thresholding using THRESH_BINARY_INV 
th2, dst2 = cv2.threshold(src, min, max, cv2.THRESH_BINARY_INV); 

# Thresholding using THRESH_TRUNC 
th3, dst3 = cv2.threshold(src, min, max, cv2.THRESH_TRUNC); 

# Thresholding using THRESH_TOZERO 
th4, dst4 = cv2.threshold(src, min, max, cv2.THRESH_TOZERO); 

# Thresholding using THRESH_TOZERO_INV 
th5, dst5 = cv2.threshold(src, min, max, cv2.THRESH_TOZERO_INV); 

# Thresholding using THRESH_TOZERO_OTSU
th6, dst6 = cv2.threshold(src, min, max,cv2.THRESH_OTSU)

# Filtrando
dst7 =  edge_sobel = filters.median(dst6)

edge_prewitt_v=filters.prewitt_v(dst7)

edge_prewitt_h=filters.prewitt_h(dst7)

edge = edge_prewitt_h + edge_prewitt_v


plt.subplot(2,4,1)
plt.imshow(src,cmap='gray')
plt.title('Origin')
plt.axis("off")

plt.subplot(2,4,2)
plt.imshow(dst1,cmap='gray')
plt.title('THRESH_BINARY')
plt.axis("off")

plt.subplot(2,4,3)
plt.imshow(dst2,cmap='gray')
plt.title('THRESH_BINARY_INV')
plt.axis("off")

plt.subplot(2,4,4)
plt.imshow(dst3,cmap='gray')
plt.title('THRESH_TRUNC')
plt.axis("off")

plt.subplot(2,4,5)
plt.imshow(dst4,cmap='gray')
plt.title('THRESH_TOZERO')
plt.axis("off")

plt.subplot(2,4,6)
plt.imshow(dst5,cmap='gray')
plt.title('THRESH_TOZERO_INV')
plt.axis("off")

plt.subplot(2,4,7)
plt.imshow(dst6,cmap='gray')
plt.title('THRESH_TOZERO_OTSU')
plt.axis("off")

plt.subplot(2,4,8)
plt.imshow(edge,cmap='gray')
plt.title('Filtramos')
plt.axis("off")


plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()


####GUINEO###
# Leer la imagen
imgray = cv2.imread("toro.jpg");

b,g,r=cv2.split(imgray)
# Calcula histograma
plt.hist(b.ravel(),256,[0,256])
plt.show()
cv2.imshow("Imagen",b)

cv2.waitKey(0)
cv2.destroyAllWindows()

####threslhold###
ret, thresh2 = cv2.threshold(b, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("threshold",thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()


#To draw all the contours in an image:
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(imgray, contours, -1, (255,0,0), 3)
cv2.imshow("images",imgray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
##To draw an individual contour, say 4th contour:
#cv2.drawContours(imgray, contours, 3, (0,255,0), 3)
#cv2.imshow("images",imgray)
#cv2.waitKey(0)
##But most of the time, below method will be useful:
#cnt = contours[4]
#cv2.drawContours(imgray, [cnt], 0, (0,255,0), 3)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
############OTSU###############################
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import coins
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
from skimage.color import lab2rgb
import matplotlib.patches as mpatches


### función para graficar imagen
def show(img, cmap=None):
    cmap = cmap or plt.cm.gray
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.imshow(img, cmap=cmap)
    ax.set_axis_off()
    plt.show()

#cargo iamgen coins
img = coins()
show(img)

##utilizo otsu para la segmentación
threshold_otsu(img)
show(img > 107)

#Clear objects connected to the label image border.
img_bin = clear_border(closing(img > 120, square(5)))
show(img_bin)

#etiqueta los objetos
labels = label(img_bin)
show(labels, cmap=plt.cm.rainbow)

### usar las regiones
regions = regionprops(labels)
boxes = np.array([label['BoundingBox'] for label in regions if label['Area'] > 100])
print(f"There are {len(boxes)} coins.")

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.imshow(img, cmap=plt.cm.gray)
ax.set_axis_off()

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

'''

#### Histogram equalization
import cv2

equ = cv2.equalizeHist(src) 
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(src)



hist = cv2.calcHist([src],[0],None,[256],[0,256])

img = cv2.imread('home.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.show()

'''