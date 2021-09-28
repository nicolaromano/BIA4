from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters.rank import minimum, median, maximum
from skimage.filters import gaussian
import matplotlib.pyplot as plt
import numpy as np

# Load the image
xray = imread("chest_xray.jpg")
# Convert to grayscale
xray = rgb2gray(xray)
xray = xray[100:500, 200:800]
print(xray.shape)

# Apply rank filters
xray_min = minimum(xray, selem = np.ones((15,15)))
xray_max = maximum(xray, selem = np.ones((15,15)))
xray_med = median(xray, selem = np.ones((15,15)))

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0,0].imshow(xray, cmap="gray")
ax[0,0].set_title("Original image", fontsize=18)
ax[0,1].imshow(xray_min, cmap="gray")
ax[0,1].set_title("Minimum filter", fontsize=18)
ax[1,0].imshow(xray_max, cmap="gray")
ax[1,0].set_title("Maximum filter", fontsize=18)
ax[1,1].imshow(xray_med, cmap="gray")
ax[1,1].set_title("Median filter", fontsize=18)

plt.show()

sigmas = [3, 5, 15]

xray_gaussian = [gaussian(xray, sigma=s) for s in sigmas]

fig, ax = plt.subplots(1, 4)

ax[0].imshow(xray, cmap="gray")

for i, s in enumerate(sigmas):
    ax[i+1].imshow(xray_gaussian[i], cmap="gray")
    ax[i+1].set_title(f"Gaussian filter - sigma={s}")

plt.show()
