import resampling
import segmentacion
import faux
import os
import numpy as np

# Pacientes id
id = 1

#Carpeta donde se almacenara los resultados
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"



imgs_after_resamp = np.load(output_path + "imgs_after_resamp_%d.npy" % (id))

masked_lung = []

for img in imgs_after_resamp:
    masked_lung.append(segmentacion.make_lungmask(img))

np.save(output_path + "maskedimages_%d.npy" % (id), masked_lung)

im = 0
graficar = []

for imag in masked_lung:
    if(im >= 160 and im <= 240):
        graficar.append(imag)
    im += 1

np.save(output_path + "graficar_%d.npy" % (id), graficar)