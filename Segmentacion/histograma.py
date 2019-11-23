import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('toro.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.plot(hist, color='gray' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.title("Histograma")

plt.show()

cv2.destroyAllWindows()