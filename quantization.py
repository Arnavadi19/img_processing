import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import downscale_local_mean

def circle_image(x, y):
    X, Y = np.meshgrid(x,y)
    radius = 0.5
    return X**2 + Y**2 <= radius**2

factors = 2**np.arange(1,5)
circ_img = circle_image(np.linspace(0,1,num=4), np.linspace(0,1,num=4))

fig, ax = plt.subplots(1, len(factors), figsize=(15,4))
for i,k in enumerate(factors):
    bins = np.linspace(0, circ_img.max(), k)
    image = np.digitize(circ_img, bins)
    image = np.vectorize(bins.tolist().__getitem__)(image - 1)
    ax[i].imshow(image)
    ax[i].set_title('$k = {}$'.format(k))

plt.show()

