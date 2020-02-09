import faux
import resampling
import os
import numpy as np

# Pacientes id
id = 1
data_path = "C:/Users/Darwin/Documents/NSCLC-RADIOMICS-INTEROBSERVER1/interobs06/02-18-2019-CT-43086/01133/"
# Carpeta donde se almacenara los resultados
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"

patient = faux.load_scan(data_path)

imgs_to_process = np.load(output_path+'fullimages_{}.npy'.format(id))

print("Slice Thickness: %f" % patient[0].SliceThickness)
print("Pixel Spacing (row, col): (%f, %f) " %
      (patient[0].PixelSpacing[0], patient[0].PixelSpacing[1]))

print("Shape before resampling\t", imgs_to_process.shape)

imgs_after_resamp, spacing = resampling.resample(
   imgs_to_process, patient, [1, 1, 1])

print("Shape after resampling\t", imgs_after_resamp.shape)

np.save(output_path + "imgs_after_resamp_%d.npy" % (id), imgs_after_resamp)