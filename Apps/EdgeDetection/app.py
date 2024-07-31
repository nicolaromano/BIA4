from shiny import App, reactive, render, ui
from skimage.io import imread
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from skimage.filters import sobel, prewitt
from skimage.feature import canny
from skimage.util import img_as_float
from scipy.ndimage import convolve

base_path = Path(__file__).parent

metadata = pd.read_csv(base_path / "metadata.csv")

imgs = {metadata.iloc[i]["title"]: img_as_float(imread(
    f"{base_path}/static/{metadata.iloc[i]['filename']}")) for i in range(metadata.shape[0])}

# Read the LoG kernels
log_kernels = np.load(f'{base_path}/static/log_kernels.npz')

app_ui = ui.page_fluid(
    ui.head_content(ui.include_css(str(base_path / "style.css"))),
    ui.h1("Edge detection", align="center"),
    ui.row(
        ui.column(3,
                  ui.div("Select an image:"),
                  offset=3, align="right"),
        ui.column(3,
                  ui.input_select("image_file", "",
                                  choices=metadata["title"].tolist(),
                                  selected=metadata.iloc[0]["title"], width="10em")
                  )
    ),
    ui.row(
        ui.column(3,
                  ui.div("Select an edge detection method:"),
                  offset=3, align="right"),
        ui.column(3,
                  ui.input_select("method", "", choices=[
                                  "Sobel", "Prewitt", "Laplacian of the Gaussian (LoG)", "Canny"], selected="Sobel", width="10em")
                  )
    ),

    ui.row(
        # Left column
        ui.column(4,
                  ui.output_plot(id="image", height="600px"),
                  ui.output_text(id="license")),
        # Middle column
        ui.column(4,
                  ui.output_plot(id="edges", height="600px"),
                  # Sobel options
                  ui.panel_conditional("input.method == 'Sobel'",
                                       ui.input_select(id="sobel_type",
                                                       label="Display",
                                                       choices=[
                                                           "Sobel X", "Sobel Y",
                                                           "Gradient magnitude", "Thresholded gradient magnitude"],
                                                       width="20em"),
                                       ui.panel_conditional("input.sobel_type == 'Thresholded gradient magnitude'",
                                                            ui.input_slider("sobel_threshold", "Threshold", min=0, max=1, step=0.01, value=0.1))),
                  # Prewitt options
                  ui.panel_conditional("input.method == 'Prewitt'",
                                       ui.input_select("prewitt_type", "Display",
                                                       choices=[
                                                           "Prewitt X", "Prewitt Y", "Gradient magnitude", "Thresholded gradient magnitude"],
                                                       width="20em"),
                                       ui.panel_conditional("input.prewitt_type == 'Thresholded gradient magnitude'",
                                                            ui.input_slider("prewitt_threshold", "Threshold", min=0, max=1, step=0.01, value=0.1))),
                  # LoG options
                  ui.panel_conditional("input.method == 'Laplacian of the Gaussian (LoG)'",
                                       ui.input_select("log_type", "Display",
                                                       choices=[
                                                           "Laplacian", "Laplacian zero-crossings", "LoG", "LoG zero-crossings"],
                                                       width="20em"),
                                       ui.panel_conditional("input.log_type == 'LoG' || input.log_type == 'Zero-crossings'",
                                                            ui.input_slider("log_sigma", "Sigma", min=1, max=10, step=0.5, value=8))),
                  # Canny options
                  ui.panel_conditional("input.method == 'Canny'",
                                       ui.input_slider(
                                           "canny_sigma", "Sigma", min=1, max=10, step=0.5, value=3),
                                       ui.input_slider(
                                           "low_threshold", "Low threshold", min=0, max=1, step=0.01, value=0.05),
                                       ui.input_slider("high_threshold", "High threshold", min=0, max=2, step=0.01, value=0.15)),
                  id="edge_column"),
        # Right column
        ui.panel_conditional("input.method == 'Sobel'",
                             ui.column(4,
                                       ui.HTML(
                                           "<div class='information'>The Sobel operator finds edges by convolving the image with a pair of 3x3 kernels designed to detect horizontal and vertical edges.<br/>The horizontal and vertical Sobel kernels are:<br/><img src='Sobel_kernels.png' width='400px' /><br /><ul><li>Each of the kernels calculates the discrete derivative of the image in a given direction; by doing this over a 3x3 neighborhood we also smooth the image, which helps to reduce noise.<br />Notice how each kernel highlights a different direction of edges.</li><li>The two resulting images are then combined to obtain the final edge map by computing the gradient magnitude (square root of the sum of the squares of the horizontal and vertical gradients).</li><li>Finally, the gradient magnitude can be thresholded to obtain a binary edge map (1-bit image).</li></ul></div>")
                                       )
                             ),
        ui.panel_conditional("input.method == 'Prewitt'",
                             ui.column(4,
                                       ui.HTML(
                                           "<div class='information'>The Prewitt operator is similar to the Sobel operator, but uses a different pair of 3x3 kernels:<br/><img src='Prewitt_kernels.png' width='400px' /><br />The Prewitt kernels don't put as much weight on the central pixel as the Sobel kernels, which makes them less sensitive to noise.<br /><ul><li>As for the Sobel kernels, each of the kernels calculates the discrete derivative of the image in a given direction; by doing this over a 3x3 neighborhood we also smooth the image, which helps to reduce noise.<br />Notice how each kernel highlights a different direction of edges.</li><li>The two resulting images are then combined to obtain the final edge map by computing the gradient magnitude (square root of the sum of the squares of the horizontal and vertical gradients).</li><li>Finally, the gradient magnitude can be thresholded to obtain a binary edge map (1-bit image).</li></ul></div>")
                                       )
                             ),
        ui.panel_conditional("input.method == 'Laplacian of the Gaussian (LoG)'",
                             ui.column(4,
                                       ui.HTML(
                                           "<div class='information'>The Laplacian of the Gaussian (LoG) operator is a tool that can be used in edge-detection algorithms (such as the Marr-Hildreth algorithm), based on the second derivative of the image.<br />Specifically, the Laplacian operator, is the sum of the second derivatives of the image in the x and y directions.<br /><img src='Laplacian.png' width='300px' /><br />The zero-crossings of this function correspond to the edges in the image.<br />This can be approximated by this kernel:<br /><img src='Laplacian_kernel.png' width='150px' /><ul><li>The LoG operator is very sensitive to noise, so it is usually applied after smoothing the image with a Gaussian filter (hence the name).</li><li>In practice, the LoG can be calculated in one go, using a kernel such as this (this is smoothing with sigma=1.4).</li><li>The LoG is <strong>anisotropic</strong>, meaning that it is sensitive to edges in all directions, an advantage compared to the Sobel and Prewitt kernels</li></ul><img src='LoG_kernel.png' width='100%' /></div>")
                                       )
                             ),
        ui.panel_conditional("input.method == 'Canny'",
                             ui.column(4,
                                       ui.HTML(
                                           "<div class='information'>The Canny edge detector is a widely used multi-step algorithm for edge detection.<br />The steps are:<br /><ol><li>Smoothing the image with a Gaussian filter to reduce noise.</li><li>Finding the intensity gradients of the image.</li><li>Suppressing non-maximum pixels (thin the edges).</li><li>Double thresholding to find potential edges.</li><li>Edge tracking by hysteresis: connecting edges that are above the high threshold and connected to an edge above the low threshold.</li></ol><br />The sigma parameter controls the amount of smoothing applied to the image before finding the gradients; try different values to see how the edge detection changes. Can you guess what is the effect of a high vs a low sigma?<br />The low and high thresholds control the minimum and maximum intensity gradient values that are considered as edges.</div>")
                                       ))
    )
)


def server(input, output, session):
    @ render.plot
    def image():
        plt.imshow(imgs[input.image_file()], cmap="gray")
        plt.title("Original image")
        plt.axis("off")

    @ render.text
    def license():
        md = metadata[metadata["title"] == input.image_file()]

        return f"Image by {md['author'].values[0]} - {md['license'].values[0]} license."

    def get_zero_crossings(img: np.ndarray) -> np.ndarray:
        """
        Gets the zero-crossings of an image (image must be a 2D array of floats)
        """
        zero_crossings = np.sign(img)

        # Zero-pad the last row and column
        # The pad_width parameter is the number of pixels to pad
        # on each side (before and after for each dimension)
        zero_crossings = np.pad(zero_crossings, pad_width=(
            (0, 1), (0, 1)), mode='constant')

        # Calculate differences between neighboring pixels
        diff_x = zero_crossings[1:-1, 1:-1] * zero_crossings[1:-1, 2:] < 0
        diff_y = zero_crossings[1:-1, 1:-1] * zero_crossings[2:, 1:-1] < 0
        diff_diag1 = zero_crossings[1:-1, 1:-1] * zero_crossings[2:, 2:] < 0
        diff_diag2 = zero_crossings[1:-1, 1:-1] * zero_crossings[2:, :-2] < 0

        # Combine differences to get zero-crossings
        return np.logical_or.reduce((diff_x, diff_y, diff_diag1, diff_diag2))

    @ render.plot
    def edges():
        edge = imgs[input.image_file()]
        if input.method() == "Sobel":
            if input.sobel_type() == "Sobel X":
                edge = sobel(edge, axis=0)
            elif input.sobel_type() == "Sobel Y":
                edge = sobel(edge, axis=1)
            elif input.sobel_type() == "Gradient magnitude":
                edge = sobel(edge)
            elif input.sobel_type() == "Thresholded gradient magnitude":
                edge = sobel(edge)
                edge = np.where(edge > input.sobel_threshold(), 1, 0)
        elif input.method() == "Prewitt":
            if input.prewitt_type() == "Prewitt X":
                edge = prewitt(edge, axis=0)
            elif input.prewitt_type() == "Prewitt Y":
                edge = prewitt(edge, axis=1)
            elif input.prewitt_type() == "Gradient magnitude":
                edge = prewitt(edge)
            elif input.prewitt_type() == "Thresholded gradient magnitude":
                edge = prewitt(edge)
                edge = np.where(edge > input.prewitt_threshold(), 1, 0)
        elif input.method() == "Laplacian of the Gaussian (LoG)":
            if input.log_type() == "Laplacian":
                kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
                edge = convolve(edge, kernel)
            elif input.log_type() == "Laplacian zero-crossings":
                kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
                edge = convolve(edge, kernel)
                edge = get_zero_crossings(edge)
            elif input.log_type() == "LoG":
                log_kernel = log_kernels[f"LoG_sigma_{input.log_sigma():0.1f}"]
                edge = convolve(edge, log_kernel)
            elif input.log_type() == "LoG zero-crossings":
                log_kernel = log_kernels[f"LoG_sigma_{input.log_sigma():0.1f}"]
                edge = convolve(edge, log_kernel)
                edge = get_zero_crossings(edge)
        elif input.method() == "Canny":
            edge = canny(edge, sigma=input.canny_sigma(
            ), low_threshold=input.low_threshold(), high_threshold=input.high_threshold())
        plt.imshow(edge, cmap="gray")

        plt.title(f"{input.method()} edge detection")
        plt.axis("off")


app = App(app_ui, server, static_assets=f"{base_path}/static")
