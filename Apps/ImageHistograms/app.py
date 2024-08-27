from shiny import App, render, ui
from skimage.io import imread
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from skimage.util import img_as_float

base_path = Path(__file__).parent

metadata = pd.read_csv(base_path / "metadata.csv")

imgs = {metadata.iloc[i]["title"]: img_as_float(imread(
    f"{base_path}/static/{metadata.iloc[i]['filename']}")) for i in range(metadata.shape[0])}

imgs_small = {k: v[::4, ::4] for k, v in imgs.items()}

app_ui = ui.page_fluid(
    ui.head_content(ui.include_css(str(base_path / "style.css"))),
    ui.h1("Image histograms", align="center"),
    ui.row(
        ui.column(3,
                  ui.div("Select an image:"),
                  offset=3, align="right"),
        ui.column(3,
                  ui.input_select("image_file", "",
                                  choices=metadata["title"].tolist(),
                                  selected=metadata.iloc[0]["title"], width="10em"),
                  )
    ),
    ui.row(
        ui.column(1,
                  ui.input_checkbox(
                      "log_histogram", "log histogram", False),
                  offset=5),
        ui.column(1,
                  ui.input_checkbox("cumulative_histogram",
                                    "Cumulative", False)
                  )
    ),
    ui.row(
        ui.column(4,
                  ui.input_slider("brightness", "Brightness", min=-100,
                                  max=100, value=0, step=1, width="100%"),
                  ui.input_slider("contrast", "Contrast", min=-100,
                                  max=100, value=0, step=1, width="100%"),
                  offset=4)
    ),

    ui.row(
        # Left column
        ui.column(4,
                  ui.output_plot(id="image", height="500px"),
                  ui.output_text(id="license")
                  ),
        # Middle column
        ui.column(4,
                  ui.output_plot(id="histogram", height="500px"),
                  ),
        # Right column
        ui.column(4,
                  ui.HTML("""
                          This app allows you to explore the histograms of different images. Explore what happens when you change the brightness and contrast of the image.<br />For example:
                          <ul>
                          <li>Select the dog image, look at the histogram and think about which part of the image contribute to each peak.</li>
                          <li>Now decrease the contrast to -30. What happens?</li><li>Put the contrast back to 0 and increase the brightness to 30. What happens (log scale might be helpful here)?</li>
                          <li>Now select the HeLa cells image. This image has three channels, so you will see three histograms. What do you see?</li>
                          <li>The image has a lot of black background, what happens when enabling the log histogram option?</li>
                          <li>This image is also very underexposed. Try increasing the brightness to 40. Do you think this is a good way to improve the image? Can you think of a better way?</li>
                          </ul>
                          """),
                  )
    )
)


def server(input, output, session):
    @ render.plot
    def image():
        img = imgs[input.image_file()]
        img = img * (1.0 + input.contrast() / 100.0) + \
            input.brightness() / 100.0
        img = np.clip(img, 0, 1)

        plt.imshow(img, cmap="gray")
        plt.title("Original image")
        plt.axis("off")

    @ render.text
    def license():
        md = metadata[metadata["title"] == input.image_file()]

        return f"Image by {md['author'].values[0]} - {md['license'].values[0]} license."

    @ render.plot
    def histogram():
        img = imgs_small[input.image_file()]

        img = img * (1.0 + input.contrast() / 100.0) + \
            input.brightness() / 100.0
        img = np.clip(img, 0.0, 1.0)

        if input.image_file() == "HeLa cells":
            fig, ax = plt.subplots(3, 1, figsize=(5, 15))
            for i, a in enumerate(ax):
                a.hist(img[:, :, i].flat, bins=512,
                       histtype="stepfilled", color=["red", "green", "blue"][i], log=input.log_histogram(), cumulative=input.cumulative_histogram())
        else:
            plt.hist(img.flat, bins=[i / 100 for i in range(101)],
                     histtype="stepfilled", color="black", log=input.log_histogram(), cumulative=input.cumulative_histogram())


app = App(app_ui, server, static_assets=f"{base_path}/static")
