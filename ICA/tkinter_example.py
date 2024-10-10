import tkinter as tk
from random import choice

# Define the function that will be called when the button is clicked
def update_counter():
    count = int(label.cget("text")) + 1
    label.config(text=str(count))
    if count % 10 == 0:
        # Every 10 clicks change the color of the label to a random color
        colours = ["red", "blue", "green", "yellow", "purple", "orange"]

        label.config(fg=colours[choice(range(len(colours)))])
    # Make the font size proportional to the count
    label.config(font=("Arial", 40 + count))

# Create the main window, 600x400 pixels
root = tk.Tk()
root.geometry("600x400")
root.title("Update the counter!")

# Create a label to display the counter
label = tk.Label(root, text="0")
# Make the font bigger. 
# The config method is used to change the properties of the widget,
# such as the text, font, color, etc.
label.config(font=("Arial", 40))
label.pack()

# Create a button. 
# When the button is clicked, the update_counter function will be called
# Note that we don't use parentheses when specifying the function name!
# This is because we are passing the function itself, 
# not the result of calling the function.
button = tk.Button(root, text="Click me!", command=update_counter)
button.pack()

# Start the main event loop
root.mainloop()
