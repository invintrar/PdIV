import faux
import numpy as np
# Pacientes id
id = 1
data_path = "C:/Users/Darwin/Documents/NSCLC-RADIOMICS-INTEROBSERVER1/interobs06/02-18-2019-CT-43086/01133/"
# Carpeta donde se almacenara los resultados
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"

patient = faxu.load_scan(data_path)
imgs = faux.get_pixels_hu(patient)

np.save(output_path + "fullimages_%d.npy" % (id), imgs)