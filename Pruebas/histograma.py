import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

#img = cv2.imread('../images/lena_color_512.tif', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('../images/lena_color_512.tif')

color = ('b', 'g', 'r')

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Lena")
plt.axis("off")


for i, c in enumerate(color):
    plt.subplot(222)
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])
    

'''
hist = cv2.calcHist([img],[0],None, [256], [0, 256])

plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title("Lena")

plt.subplot(122)
plt.plot(hist, color='gray')
plt.xlabel('Intensidad')
plt.ylabel('Pixeles')
'''
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()