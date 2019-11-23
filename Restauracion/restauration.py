import matplotlib.pyplot as plt
import numpy as np
import fuctionR


[imgO,imgN, imgR] = fuctionR.wiener()
#[imgO,imgN, imgR] = fuctionR.unwarapPhase()
#[imgO,imgN, imgR] = fuctionR.cspin()
#[imgO,imgN, imgR] = fuctionR.denoiseNlMeans()
#[imgO,imgN, imgR] = fuctionR.denoiseTvBregman()
#[imgO,imgN, imgR] = fuctionR.deoniseTvChambolle()
#[imgO,imgN, imgR] = fuctionR.denoiseWavelet()
#[imgO,imgN, imgR] = fuctionR.deoniseBilateral()
#[imgO,imgN, imgR] = fuctionR.estimateSigma()
#[imgO,imgN, imgR] = fuctionR.inpaintBiharmonic()
#[imgO,imgN, imgR] = fuctionR.richardsonLucy()
#[imgO,imgN, imgR] = fuctionR.unSupervisedWiener()


#Mostramos las imagenes
plt.subplot(221), plt.imshow(imgO,cmap='gray'), plt.title('Original')
plt.axis('off')
plt.subplot(222), plt.imshow(imgN,cmap='gray'), plt.title('Noise')
plt.axis('off')
plt.subplot(223), plt.imshow(imgR,cmap='gray'), plt.title('Restauration')
plt.axis('off')
plt.show()