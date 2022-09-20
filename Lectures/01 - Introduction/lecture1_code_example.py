# In this example coding session we will
# 1. Load an image from file
# 2. Inspect the image and show it with different colourmaps

import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np

nuclei = imread("nuclei1.tif")

print(type(nuclei))
print(nuclei.shape)
print(nuclei.dtype)
print(f"Minimum: {np.min(nuclei)} - Maximum: {np.max(nuclei)}")

plt.imshow(nuclei, cmap="gray")
plt.title("Nuclei stained with DAPI", fontsize = 18)
plt.axis("off")
plt.show()
