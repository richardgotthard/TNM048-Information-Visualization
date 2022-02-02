from multiprocessing import dummy
import pandas as pd
import tkinter
from tkinter import filedialog
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import *   
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk) 
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_agg import FigureCanvasAgg
import tkinter

#choose datset using tkinter askopenfilename()
Tk().withdraw() 
filename = askopenfilename() 
print("You chose: %s" % filename)

#case of the two given datasets of not having a header
df = pd.read_csv(filename, header=None)

#print and show the dataset that was choosen
print("This is your dataset:\n")
print(df)

# get min and max values of dataset (first x (column '0') then y (column '1'))
max_value_x = df[0].max()
min_value_x = df[0].min()
max_value_y = df[1].max()
min_value_y = df[1].min()

#future margins for the minimal and maximum values x and y
min_max_distance_x = math.ceil(abs((max_value_x - min_value_x))) # change 1.1 to accomadet size (size of screen?)
min_max_distance_y = math.ceil(abs((max_value_y - min_value_y))) # keep in mind to also change the points accordingly

# convert dataframe column to list to be able to iterate 
x_value_list = df[0].tolist()
y_value_list = df[1].tolist()
category_list = df[2].tolist()

#--------------starting to create the canvas to plot the dataset
# https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html
# fig = Figure(figsize=(5, 4), dpi=100)

# canvas = FigureCanvasAgg(fig)

# ax = fig.add_subplot()

# ax.plot([1, 2, 3])

# canvas.draw()
# fig.canvas.draw_idle()

# https://stackoverflow.com/questions/50165115/unable-to-call-canvas-show
# GUI Set-Up
# f = Frame(root)
# plt.style.use('ggplot')
# fig = Figure(figsize=(12, 7), dpi=100)

# a = fig.add_subplot()
# a.set_title("Scatter plot of choosen data")

# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
# canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

# Frame.pack(f)

root = tkinter.Tk()
root.wm_title("Scatter plot")

fig = Figure(figsize=(8, 6), dpi=100)

#t = np.arange(min_value_x, max_value_x, .01) # (start of x to end of x, interval )

ax = fig.add_subplot()

ax.legend()

for i in range(len(x_value_list)):
    if category_list[i] == "a" or category_list[i] == "foo":
      line, = ax.plot(x_value_list[i], y_value_list[i], color='red', marker='o')
    if category_list[i] == "b" or category_list[i] == "baz":
      line, = ax.plot(x_value_list[i], y_value_list[i], color='green', marker='o')
    if category_list[i] == "c" or category_list[i] == "bar":
      line, = ax.plot(x_value_list[i], y_value_list[i], color='blue', marker='o')

ax.set_xlabel("x value/position")
ax.set_ylabel("y value/position")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tkinter.Button(master=root, text="Quit", command=root.quit)

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button_quit.pack(side=tkinter.BOTTOM)
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()









