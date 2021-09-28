# In this example coding session we will
# 1. Load an image from file
# 2. Inspect the image and show it with different colourmaps

from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np

nuclei = imread("nuclei1.tif")

print(type(nuclei))
print(nuclei.shape)
print(nuclei.dtype)
print(np.max(nuclei))

plt.imshow(nuclei, cmap="gray")
plt.axis("off")
plt.title("Cell nuclei stained with DAPI", fontsize=18)
plt.show()
