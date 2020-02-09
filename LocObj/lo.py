from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

plt.rcParams['image.cmap'] = 'gray'


image = io.imread('guante.png')

image = image/255

print("Dimensiones de la image: %s" % str(image.shape))

h, w, c = image.shape

print("Tipo de los elementos de la imagen: %s" % str(image.dtype))

'''
plt.imshow(image)

green=np.copy(image)
green[:,:,0]=0
green[:,:,2]=0
plt.figure()
plt.imshow(green)

red=np.copy(image)
red[:,:,1:3]=0
plt.figure()
plt.imshow(red)

blue=np.copy(image)
blue[:,:,0:2]=0
plt.figure()
plt.imshow(blue)
'''

image_hsv = matplotlib.colors.rgb_to_hsv(image)
print("El pixel de la posición (100,100) se codifica en RGB como %s " %
      str(image[100, 100, :]))
print("El pixel de la posición (100,100) se codifica en HSV como %s " %
      str(image_hsv[100, 100, :]))

'''
plt.figure()
plt.imshow(image_hsv[:, :, 0])
plt.colorbar()

plt.figure()
plt.imshow(image_hsv[:, :, 1])
plt.colorbar()

plt.figure()
plt.imshow(image_hsv[:, :, 2])
plt.colorbar()

h_min, h_max = (230/255, 250/255)
s_min, s_max = (100/255, 230/255)
v_min, v_max = (50/255, 170/255)
'''

h, w, c = image_hsv.shape
segmentation_mask = np.zeros((h, w))

for i in range(h):  # evitamos los bordes
    for j in range(w):  # evitamos los bordes
        h_val, s_val, v_val = image_hsv[i, j, :]
        # IMPLEMENTAR
        # Si los valores están en rango, poner en 1 la coordenada (i,j) de la máscara de segm


#plt.imshow(segmentation_mask, vmin=0, vmax=1)

# erosionar la mascara 
for i in range(1,h-1):#evitamos los bordes
    for j in range(1,w-1): #evitamos los bordes
        #IMPLEMENTAR
        #Contar cuantos pixeles blancos hay entre entre el pixel (i,j) 
        #y sus vecinos inmediatos
        pass

plt.imshow(eroded_mask,vmin=0,vmax=1) 

plt.show()
