from shiny import App, reactive, render, ui
from skimage.io import imread
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

base_path = Path(__file__).parent

files = list(base_path.glob("dog_*.png"))
bit_depths = ["1", "2", "4", "8"]
imgs = {bd: imread(str(base_path / f"dog_{bd}bit.png")) for bd in bit_depths}

mousex = reactive.value(100)
mousey = reactive.value(100)

app_ui = ui.page_fluid(
    ui.h1("Bit Depth of an Image", align="center"),
    ui.row(
        ui.column(2,
                  ui.div("Select the bit depth of the image:"),
                  offset=4, align="right"),
        ui.column(2,
                  ui.input_select("bit_depth", "",
                                  choices=bit_depths,
                                  selected="8", width="5em"),
                  )
    ),
    ui.row(
        ui.column(4,
                  ui.output_plot(id="image", width=400, click=True),
                  offset=2),
        ui.column(3,
                  ui.card(
                      ui.div(
                          "Click on the image to see the pixel values around the cursor."),
                      ui.output_text_verbatim(id="matrix"))
                  )
    ),
    ui.row(
        ui.column(4,
                  ui.output_table(id="summary"),
                  offset=2)
    )
)


def server(input, output, session):
    @render.plot
    def image():
        plt.imshow(imgs[input.bit_depth()], cmap="gray")

        plt.scatter(mousex(), mousey(), s=30, c="red")
        plt.axis("off")

    @render.text
    def matrix():

        if input.image_click():
            coords = input.image_click()
            mousex.set(int(coords["x"]))
            mousey.set(int(coords["y"]))

        matrix = imgs[input.bit_depth()][mousey() - 5:mousey() +
                                         5, mousex() - 5:mousex() + 5]
        return matrix
    
    @render.table
    def summary():
        img = imgs[input.bit_depth()]

        return pd.DataFrame({
            "Image Min": [img.min()],
            "Image Max": [img.max()],
            "Image Mean": [img.mean().round(2)],
            "Image SD": [img.std().round(2)]
        })

app = App(app_ui, server)
