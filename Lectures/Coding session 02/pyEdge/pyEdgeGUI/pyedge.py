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
import PySimpleGUI as sg

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

# The layout for our window
layout = [
    [sg.Text("Edge detection")],
    [sg.Text("Input image"), sg.FileBrowse(key="input_image")],
    [sg.Text("Colourmap"), sg.Combo(["gray", "viridis", "Greens", "Reds", "Blues"], key="colourmap", default_value="gray", readonly=True)], 

    [sg.Checkbox("Save to file", default=False, key="save_file"), sg.Text("Output file name"), 
        sg.InputText(default_text = "edges.png", key="output_file")],
    [sg.Text("Method"), sg.Combo(["canny", "sobel", "prewitt"], key="method", default_value="canny", readonly=True), 
        sg.Button("Detect edges")], 
    [sg.Button("Exit")]
    ]

window = sg.Window("pyEdge", layout=layout)

while(True):
    event, values = window.read()
    
    if event=="Exit" or event==sg.WIN_CLOSED:
        window.close()
        break
    elif event=="Detect edges":
        if values['input_image'] == "": # We have not chosen a file yet
            sg.popup("Please choose a file first")
        else:
            img = imread(values['input_image'])
            img_edges = find_edges(img, values['method'])
            display_images(img, img_edges, values['colourmap'])
            if values['save_file'] == True:
                imsave(fname=values['output_file'], arr=img_edges)

# # TODO: these should be passed by the user
# # if no output filename is passed, it should be generated automatically
# input_filename = "test_images/DAPI.png"
# output_filename = "test_images/DAPI_edges.png"

# # Read image and find edges

# # TODO: user should choose method
# 

# # Save to file
# 

# 