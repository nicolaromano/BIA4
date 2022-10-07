""" 
pyEdge: a small utility to detect edges in images.
It supports three different methods for edge detection: Canny, Sobel and Prewitt
"""

# Import libraries
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.filters import sobel, prewitt
from skimage.feature import canny
import numpy as np

# Functions

def find_edges(img:np.array, method:str="canny") -> np.array:
    """Finds edges in an image, using the method chosen by the user (default is Canny)

    Args:
        img (np.array): The input image
        method (str, optional): The edge-detection method. Defaults to "canny".
                                Allowed values are "canny", "prewitt", "sobel".

    Returns:
        np.array: The detected edges
    """

    if method == "canny":
        img_edges = canny(img, sigma = 7)
    elif method == "sobel":
        img_edges = sobel(img)
    elif method == "prewitt":
        img_edges = prewitt(img)
    else:
        raise ValueError(f"{method} is not a recognised method.")

    return img_edges

def display_images(img:np.array, img_edges:np.array, cmap:str="gray")-> None:
    """Displays the image and the edges side by side

    Args:
        img (np.array): The input image
        img_edges (np.array): The image of the edges
        cmap (str): The colourmap. Default is gray

    Returns: None - displays the images
    """

    # Display images
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    ax[0].imshow(img, cmap=cmap)
    ax[1].imshow(img_edges, cmap=cmap)

    for a in ax:
        a.axis("off")

    plt.show()


# TODO: these should be passed by the user
# if no output filename is passed, it should be generated automatically
input_filename = "test_images/DAPI.png"
output_filename = "test_images/DAPI_edges.png"

# Read image and find edges
img = imread(input_filename)

# TODO: user should choose method
img_edges = find_edges(img, "sobel")

# Save to file
imsave(fname=output_filename, arr=img_edges)

display_images(img, img_edges, "gray")