import numpy as np 
import statistics as sta
import cv2 as cv
from matplotlib import pyplot as plt 

#img = cv.imread('./nlm_patch.jpg')
#img1 = cv.imread('./images/geeks14.png',0)

#cv.imshow('image',img1)
#N = 2
#dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
#a = np.array([[0.9361, 1.000, 1.000, 0.8871], [1.000, 1.000, 0.9184, 1.000], [0.9868, 1.000, 1.000, 0.9591], [0.000, 0.8987, 0.9400, 1.000]])
#b = np.zeros((6,6))
#b[1:-1,1:-1] = a

#a = np.random.rand(N,N)
#b = np.zeros((N+2,N+2))
#b[1:-1,1:-1] = a

#lista =np.array([[1, 2, 3],[4, 0.7, 2.000],[0.8, 3.000, 2.5]])
vector = [1,3,4,2,0.5,2,5]
lista = np.array(vector)
vmax = lista.max()
vmin = lista.min()
vmed = sta.median(lista)
print(vmax)
print(vmed)
print(vmin)




#media = lista.mean()
#print(B)
#varianza = lista.var()
#desviacion = lista.std()
#print(media,varianza,desviacion)

#plt.subplot(1,2,1)
#plt.imshow(img)
#plt.subplot(1,2,2), plt.imshow(dst)
#plt.show()

# Wait for keyboard
cv.waitKey(0)
cv.destroyAllWindows()