import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
import fanoise 
import filtros


# Load una imagen
img = cv2.imread("./lena.bmp",0)

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")

# Agrego Ruido gausiano a la imagen
gauss = fanoise.noiseG(img, 0.3, 0.01)

# Agrego Ruido Sal Pimiento
nsp = fanoise.salpim(img)

""" Filtramos la imagen con ruido """ 
# Arimetico 3x3
imgA = filtros.aritmetica(gauss)
# Geometrica 3x3
imgG = filtros.geometrica(gauss)
# Armonico 3x3
imgAm = filtros.armonica(gauss)
#Contra Armonica 3x3
imgCam = filtros.charmonic(gauss) 
# Adaptive local noise reduction
imgAlr = filtros.alnr(gauss,0.01)   
# Adaptive mean 
imgAm = filtros.am(gauss)
   
       
# View image
plt.figure()
plt.subplot(3,3,1)
plt.title("Lena Original")
plt.imshow(img,cmap='gray')
plt.axis('off')

plt.subplot(3,3,2)
plt.title("Ruido Gauss")
plt.imshow(gauss,cmap='gray')
plt.axis('off')

plt.subplot(3,3,3)
plt.title("Sal y Pimiento")
plt.imshow(nsp,cmap='gray')
plt.axis('off')
'''
plt.subplot(3,3,4)
plt.title("Histograma")
plt.hist(gauss.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.axis('off')
'''
plt.subplot(3,3,4)
plt.title("Filtro Aritmetico")
plt.imshow(imgA,cmap='gray')
plt.axis('off')

plt.subplot(3,3,5)
plt.title("Filtro Geometrico")
plt.imshow(imgG, cmap='gray')
plt.axis('off')

plt.subplot(3,3,6)
plt.title("Filtro Armonico")
plt.imshow(imgAm,cmap='gray')
plt.axis('off')

plt.subplot(3,3,7)
plt.title("Filtro Contra Armonica")
plt.imshow(imgCam,cmap='gray')
plt.axis('off')

plt.subplot(3,3,8)
plt.title("Adaptive, local noise reduction filter")
plt.imshow(imgAlr,cmap='gray')
plt.axis('off')

plt.subplot(3,3,9)
plt.title("Adaptative mean filter")
plt.imshow(imgAm,cmap='gray')
plt.axis('off')

plt.show()

# Wait for keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
