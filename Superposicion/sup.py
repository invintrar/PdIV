from skimage.io import imread, imshow
import matplotlib.pyplot as plt 

image_gray = imread('image/yo4.png', as_gray=True)
imshow(image_gray)

plt.show()