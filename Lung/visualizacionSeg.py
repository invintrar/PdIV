import numpy as np
import segmentacion
import displaySt

# Pacientes id
id = 1
# Carpeta donde se almacenara los resultados
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"


imgs_after_resamp = np.load(output_path + "imgs_after_resamp_%d.npy" % (id))

masked_lung = np.load(output_path + "maskedimages_%d.npy" % (id))


displaySt.sample_stack(masked_lung, show_every=10)

img = imgs_after_resamp[210]
segmentacion.make_lungmask(img, display=True)