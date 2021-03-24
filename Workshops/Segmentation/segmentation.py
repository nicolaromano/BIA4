import numpy as np
from skimage.io import imread, imshow, imsave
import matplotlib.pyplot as plt

cells = imread("cells_segm.tif", plugin="tifffile")

print(cells.shape)

imshow(cells)
plt.show()

nuclei = cells[:, :, 2]
fig, ax = plt.subplots(ncols=2, nrows=1)

from skimage.filters import threshold_otsu, threshold_li, threshold_local, threshold_niblack

nuclei_threshold_otsu = nuclei > threshold_otsu(nuclei)
nuclei_threshold_li = nuclei > threshold_li(nuclei)
nuclei_threshold_niblack = nuclei > threshold_niblack(nuclei)
# Local threshold needs a block size (which MUST be an odd number)!
nuclei_threshold_local = nuclei > threshold_local(nuclei, block_size=11)