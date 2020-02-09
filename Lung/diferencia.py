import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# Pacientes id
id = 1

# Carpeta donde se almacenara los resultados
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"
imgs_after_resamp = np.load(output_path + "imgs_after_resamp_%d.npy" % (id))
masked_lung = np.load(output_path + "maskedimages_%d.npy" % (id))

# Cargamos las dos imagenes para hacer las diferencias
diff1 = imgs_after_resamp[210]
im_fin = np.uint8(diff1)
res_img = Image.fromarray(im_fin, mode="L")
res_img.save(output_path + "image%d.jpg" % (id))
diff2 = masked_lung[210]
diff3 = masked_lung[100]
diff_total = abs(diff2 - diff3)


fig, ax = plt.subplots(1,3)
ax[0].imshow(diff2)
ax[0].set_title("Slice 210")
ax[0].axis('off')
ax[1].imshow(diff3)
ax[1].set_title("Slice 100")
ax[1].axis('off')
ax[2].imshow(diff_total)
ax[2].set_title("Diferecia")
ax[2].axis('off')


plt.show()
