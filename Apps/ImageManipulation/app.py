from shiny import App, reactive, render, ui
from skimage.io import imread
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
from pprint import pformat

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
                  ui.output_plot(id="image", width=400, hover=True),
                  offset=2),
        ui.column(3,
                  ui.card(
                      ui.div(
                          "Move the mouse on the image to see the pixel values around the dot."),
                      ui.output_text_verbatim(id="matrix"))
                  )
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

        if input.image_hover():
            coords = input.image_hover()
            mousex.set(int(coords["x"]))
            mousey.set(int(coords["y"]))

        matrix = imgs[input.bit_depth()][mousey() - 5:mousey() +
                                         5, mousex() - 5:mousex() + 5]
        return matrix


# with ui.layout_column_wrap(gap="2rem"):
#     ui.output_plot(width=300, hover=True)

#     def image():
#         plt.imshow(imgs[input.bit_depth()], cmap="gray")
#         plt.axis("off")

#     with ui.card():
#         ui.div("Move the mouse on the image to see the pixel values around the dot.")

#         @render.ui
#         def matrix():
#             matrix = imgs[input.bit_depth()][400:420, 150:160]

#             def format_row(row):
#                 return " ".join("{:>3}".format(num) for num in row)

#             return ui.div([ui.div({"style": "font-size: 0.8rem; font-family: 'monospace'"},
#                                   format_row(row)) for row in matrix])


# @render.table
# def summary():
#     bit_depths = {
#         1: "1-bit",
#         2: "2-bit",
#         4: "4-bit",
#         "uint8": "8-bit",
#     }

#     img = imgs[input.bit_depth()]

#     return pd.DataFrame({
#         "Image Min": [img.min()],
#         "Image Max": [img.max()]
#     })

app = App(app_ui, server)
