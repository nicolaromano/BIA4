from tkinter import Tk, Button, Label
from tkinter import filedialog
from skimage import io, color, filters
from skimage.feature import canny
import matplotlib.pyplot as plt
# We need to import this to convert the image to a format 
# that can be displayed in the GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

filename = "cells.jpg"
img = io.imread(filename)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img, cmap='gray')
ax[0].axis('off')
ax[1].imshow(canny(color.rgb2gray(img)), cmap='gray')
ax[1].axis('off')

# Put the figure on a "canvas" widget
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root = Tk()
root.title('Image Viewer')
root.geometry('800x600')

root.mainloop()