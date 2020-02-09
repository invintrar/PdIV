import os
import numpy as np
import matplotlib.pyplot as plt

id = 0;
output_path = "C:/Users/Darwin/Documents/ResultadosNSCL/"

for x in range(18):
    file_used=output_path+"fullimages_%d.npy" % id
    imgs_to_process = np.load(file_used).astype(np.float64) 

    plt.hist(imgs_to_process.flatten(), bins=50, color='c')
    plt.title("Paciente %d " % (x))
    plt.xlabel("Hounsfield Units (HU)")
    plt.ylabel("Frequency")
    plt.show()