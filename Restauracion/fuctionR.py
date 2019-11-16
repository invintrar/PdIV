import numpy as np
import skimage.data
from skimage.util import random_noise 
from skimage import img_as_float
from scipy.signal import convolve2d
from skimage import color, data, restoration, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma, inpaint_biharmonic, estimate_sigma, denoise_bilateral, denoise_wavelet, unwrap_phase,denoise_wavelet,cycle_spin,denoise_tv_bregman,denoise_tv_chambolle


def denoiseNlMeans():
    a = np.zeros((40, 40))
    a[10:-10, 10:-10] = 1.
    imgO = a.copy()
    a += 0.3 * np.random.randn(*a.shape)
    imgN = a.copy()
    denoised_a = denoise_nl_means(a, 7, 5, 0.1)
    imgR = denoised_a.copy()
        
    return [imgO, imgN, imgR]

def denoiseTvBregman():
    a = np.zeros((40, 40))
    a[10:-10, 10:-10] = 1.
    imgO = a.copy()
    a += 0.3 * np.random.randn(*a.shape)
    imgN = a.copy()
    denoised_a = denoise_tv_bregman(a, 7, 5, 0.1)
    imgR = denoised_a.copy()
    
    return [imgO, imgN, imgR]

def deoniseTvChambolle():
    img = color.rgb2gray(data.astronaut())[:50, :50]
    imgO = img.copy()
    img += 0.5 * img.std() * np.random.randn(*img.shape)
    imgN = img.copy()
    denoised_img = denoise_tv_chambolle(img, weight=60)
    imgR = denoised_img.copy()
    
    return [imgO, imgN, imgR]


def denoiseWavelet():
    img = img_as_float(data.astronaut())
    img = color.rgb2gray(img)
    imgO = img.copy()
    img += 0.1 * np.random.randn(*img.shape)
    img = np.clip(img, 0, 1)
    imgN = img.copy()
    denoised_img = denoise_wavelet(img, sigma=0.1, rescale_sigma=True)
    imgR = denoised_img.copy()
    
    return [imgO, imgN, imgR]


def deoniseBilateral():
    astro = img_as_float(data.astronaut())
    astro = astro[220:300, 220:320]
    imgO = astro.copy()
    noisy = astro + 0.6 * astro.std() * np.random.random(astro.shape)
    noisy = np.clip(noisy, 0, 1)
    imgN = noisy.copy()
    denoised = denoise_bilateral(noisy, sigma_color=0.05, sigma_spatial=15,
                             multichannel=True)
    imgR = denoised.copy()
    
    return [imgO, imgN, imgR]


def estimateSigma():
    img = img_as_float(skimage.data.camera())
    imgO = img.copy()
    sigma = 0.01
    img = img + sigma * np.random.standard_normal(img.shape)
    imgN = img.copy()
    sigma_hat = estimate_sigma(img, multichannel=False)
    imgR = sigma_hat.copy()
    
    return [imgO, imgN, imgR]


def inpaintBiharmonic():
    img = np.tile(np.square(np.linspace(0, 1, 5)), (5, 1))
    imgO = img.copy()
    mask = np.zeros_like(img)
    mask[2, 2:] = 1
    mask[1, 3:] = 1
    mask[0, 4:] = 1
    imgN = mask.copy()
    out = inpaint_biharmonic(img, mask)
    imgR = out.copy()
    return [imgO, imgN, imgR]

def richardsonLucy():
    camera = color.rgb2gray(data.camera())
    imgO = camera.copy()
    
    psf = np.ones((5, 5)) / 25
    camera = convolve2d(camera, psf, 'same')
    camera += 0.1 * camera.std() * np.random.standard_normal(camera.shape)
    imgN = camera.copy()
    
    deconvolved = restoration.richardson_lucy(camera, psf, 5)
    imgR = deconvolved.copy()

    return [imgO, imgN, imgR]

def cspin():
    img = img_as_float(skimage.data.camera())
    imgO = img.copy()
    sigma = 0.1
    img = img + sigma * np.random.standard_normal(img.shape)
    imgN = img.copy()
    denoised = cycle_spin(img, func=denoise_wavelet, max_shifts=3)
    imgR = denoised.copy()
    
    return [imgO, imgN, imgR]
    
def unwarapPhase():
    c0, c1 = np.ogrid[-1:1:128j, -1:1:128j]
    image = 12 * np.pi * np.exp(-(c0**2 + c1**2))
    imgO = image.copy()
    image_wrapped = np.angle(np.exp(1j * image))
    imgN = image.copy()
    image_unwrapped = unwrap_phase(image_wrapped)
    imgR = image.copy()
    np.std(image_unwrapped - image) < 1e-6   # A constant offset is normal
    
    return [imgO, imgN, imgR]

def wiener():
    img = color.rgb2gray(data.astronaut())
    imgO = img.copy()
    psf = np.ones((5, 5)) / 25
    img = convolve2d(img, psf, 'same')
    img += 0.1 * img.std() * np.random.standard_normal(img.shape)
    imgN = img.copy()
    deconvolved_img = restoration.wiener(img, psf, 1100)
    imgR = img.copy()
    
    return [imgO, imgN, imgR]

def unSupervisedWiener():
    img = color.rgb2gray(data.astronaut())
    imgO = img.copy()
    
    psf = np.ones((5, 5)) / 25
    img = convolve2d(img, psf, 'same')
    img += 0.1 * img.std() * np.random.standard_normal(img.shape)
    imgN = img.copy()
    
    deconvolved_img = restoration.unsupervised_wiener(img, psf)
    imgR = deconvolved_img.cpy()
    
    return [imgO, imgN, imgR]