import numpy as np
import matplotlib.pyplot as plt
# from skimage.io import imshow, imread
# Image sampling involves taking the value of the image at regular spatial intervals.
# The length of the intervals defines the spatial resolution of the image.

def circle_image(x, y): # result is a 2D array representing a circular region where the value is True inside the circle and False outside
    X, Y = np.meshgrid(x, y) #meshgrid of x and y points in the coordinate axes direction
    radius  = 0.5
    return X**2 + Y**2 <= radius**2

factors = 2**np.arange(1,5) 
#numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
#Return evenly spaced values within a given interval.
fig, ax = plt.subplots(1, len(factors), figsize=(15,4))

for i,N in enumerate(factors):
    x = np.linspace(-1, 1, num=N)
    y = np.linspace(-1, 1, num=N)
    image = circle_image(x, y)
    ax[i].imshow(image, cmap='gray')
    ax[i].set_title('$N = {}$'.format(N))

plt.show()


