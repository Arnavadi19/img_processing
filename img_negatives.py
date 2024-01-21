import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/arnav/Documents/DIP/practice/pizza.jpg', cv.IMREAD_GRAYSCALE)
plt.figure(figsize=(7,7))
plt.axis('on')
plt.imshow(img, cmap='gray')
plt.show()

#let L be the maximum intensity in the image.
# neg_img = L - 1 - img
L = img.max()
neg_img = L - 1 - img
plt.figure(figsize=(7,7))
plt.axis('on')
plt.imshow(neg_img, cmap = 'gray')
plt.show()