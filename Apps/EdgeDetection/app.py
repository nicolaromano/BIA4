from shiny import App, reactive, render, ui
from skimage.io import imread
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from skimage.filters import sobel, prewitt, laplace
from skimage.feature import canny

base_path = Path(__file__).parent

metadata = pd.read_csv(base_path / "metadata.csv")

imgs = {metadata.iloc[i]["title"]: imread(
    f"{base_path}/static/{metadata.iloc[i]["filename"]}") for i in range(metadata.shape[0])}

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
                  ui.output_plot(id="image", height="650px"),
                  ui.output_text(id="license")),
        # Middle column
        ui.column(4,
                  ui.output_plot(id="edges", height="650px"),
                  # Sobel options
                  ui.panel_conditional("input.method == 'Sobel'",
                                       ui.input_select(id="sobel_type",
                                                       label="Sobel type",
                                                       choices=[
                                                           "Sobel X", "Sobel Y",
                                                           "Gradient magnitude", "Thresholded gradient magnitude"],
                                                       width="20em")),
                  ui.panel_conditional("input.method == 'Sobel' && input.sobel_type == 'Thresholded gradient magnitude'",
                                       ui.input_slider("sobel_threshold", "Threshold", min=0, max=1, step=0.01, value=0.1)),
                  # Prewitt options
                  ui.panel_conditional("input.method == 'Prewitt'",
                                       ui.input_select("prewitt_type", "Prewitt type",
                                                       choices=[
                                                           "Prewitt X", "Prewitt Y", "Gradient magnitude", "Thresholded gradient magnitude"],
                                                       width="20em")),
                  ui.panel_conditional("input.method == 'Prewitt' && input.prewitt_type == 'Thresholded gradient magnitude'",
                                       ui.input_slider("prewitt_threshold", "Threshold", min=0, max=1, step=0.01, value=0.1)),
                  # LoG options
                  ui.panel_conditional("input.method == 'Laplacian of the Gaussian (LoG)'",
                                       ui.input_slider("log_sigma", "Sigma", min=0.1, max=5, step=0.1, value=1)),
                  # Canny options
                  ui.panel_conditional("input.method == 'Canny'",
                                       ui.input_slider(
                                           "canny_sigma", "Sigma", min=1, max=20, step=0.5, value=5),
                                       ui.input_slider(
                                           "low_threshold", "Low threshold", min=0, max=10, step=0.5, value=2),
                                       ui.input_slider("high_threshold", "High threshold", min=0, max=30, step=0.5, value=5)),
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
                                )
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
            edge = laplace(edge, ksize=int(input.log_sigma()))            
        elif input.method() == "Canny":
            edge = canny(edge, sigma=input.canny_sigma(), low_threshold=input.low_threshold(), high_threshold=input.high_threshold())
        plt.imshow(edge, cmap="gray")

        plt.title(f"{input.method()} edge detection")
        plt.axis("off")


app = App(app_ui, server, static_assets=f"{base_path}/static")
