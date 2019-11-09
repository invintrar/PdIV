from skimage.util import random_noise
import cv2

def noiseG(img,media, varianza):
    imgn = img.copy() 
    # Gaussian distribution parameters
    #localv = random_noise(imgr, mode='localvar', seed=None, clip=True)
    #pois = random_noise(imgr, mode='poisson', seed=None, clip=True)
    gauss = random_noise(imgn, mode='gaussian', seed=None, clip=True, mean=media, var= varianza)
    return gauss
    
def salpim(img):
    imgsp = img.copy()
    nsp = random_noise(imgsp, mode='s&p', seed=None, clip=True,amount=0.06)
    return nsp