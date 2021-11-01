"""
pyEdge: a small utility to detect edges in images
"""

# Import libraries
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.feature import canny
from skimage.filters import sobel, prewitt
import sys
import argparse as ap
import PySimpleGUI as sg


def plot_results(img, img_edges, cmap="gray"):
    """Plots the results of edge detection

    Args:
        img (np.array): The original image
        img_edges (np.array): The detected edges
        cmap (str, optional): The colourmap. Defaults to "gray".

    Returns: nothing
    """
    # Display
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax[0].imshow(img, cmap=cmap)
    ax[1].imshow(img_edges, cmap=cmap)

    for a in ax:
        a.axis("off")

    plt.show()


def detect_edges(img, method="canny"):
    """Detect edges in an image

    Args:
        img (np.array): The image
        method (str, optional): The edge-detecting algorithm. Defaults to "canny".

    Returns (np.array): The edges of the image
    """

    if method == "canny":
        return canny(img, sigma=7)
    elif method == "prewitt":
        return prewitt(img)
    elif method == "sobel":
        return sobel(img)
    else:
        sys.exit(f"{method} is an unsupported edge-detecting method!")


sg.theme("DarkTeal7")

# The layout of our GUI
layout = [
    [sg.Text("Edge detection")],    
    [sg.Text("Input image"), sg.FileBrowse(key="input_image")],
    [sg.Text("Method"), sg.Combo(["canny", "prewitt", "sobel"],
                                 key="method", default_value="canny")],    
    # Add an input text field called "Output image" with key output_image
    [sg.Text("Output image"), sg.InputText(key="output_image")],
    [sg.Button("Detect edges"), sg.Button("Exit")]
]

while(True):
    event, values = sg.Window("Edge detection", layout).read()
    if event == "Exit":
        sg.Window.close()
        break
    elif event == "Detect edges":
        if values["input_image"] == "":
            sg.popup("Please select an input image!")
            continue        
        # Read the image
        img = imread(values["input_image"])
        # Detect edges
        img_edges = detect_edges(img, values["method"])
        # Plot the results
        plot_results(img, img_edges)
        # Save the image
        out = values["output_image"]
        if out == "":
            out = values['input_image'].split(".")[0] + "_edges." + values['input_image'].split(".")[1]

        imsave(out, img_edges)    