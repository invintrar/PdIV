import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import numpy as np
import segm


img1 = cv2.imread("paisaje.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)
[io1,r1]=segm.obtenerI(img)

img1 = cv2.imread("100.bmp")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)
[io2,r2]=segm.obtenerI(img)

img1 = cv2.imread("outdoor.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)
[io3,r3]=segm.obtenerI(img)

img1 = cv2.imread("triangulo.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)
[io4,r4]=segm.obtenerI(img)

figure_size = 15
plt.figure(figsize=(figure_size,figure_size))

plt.subplot(2,4,1),plt.imshow(io1)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2),plt.imshow(io2)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3),plt.imshow(io3)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4),plt.imshow(io4)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

K=10
plt.subplot(2,4,5),plt.imshow(r1)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6),plt.imshow(r2)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7),plt.imshow(r3)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8),plt.imshow(r4)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])

plt.show()