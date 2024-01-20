import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread, imshow
from skimage.transform import downscale_local_mean

pizza  = imread('pizza.jpg')
factors = 3**np.arange(1,5)
figure, axis = plt.subplots(1, len(factors), figsize=(20,6))

for factor, ax in zip(factors,axis):
    image = downscale_local_mean(pizza, factors = (factor, factor, 1)).astype(int)

    ax.imshow(image)
    ax.set_title('$N={}$'.format(image.shape[0]))

plt.show()

