from multiprocessing import dummy
import pandas as pd
import tkinter
from tkinter import filedialog
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import *   
import math
import matplotlib
from matplotlib.figure import Figure


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

#starting to create the canvas to plot the dataset

#get screen size of current device
root = tkinter.Tk()
width_screen = root.winfo_screenwidth() #1440
height_screen = root.winfo_screenheight() #900

# set size of window (fullscreen) and title
screen_resolution = str(width_screen)+'x'+str(height_screen)
root.geometry(screen_resolution) # (width x height) size of the window
root.title('Scatterplot of dataset choosen')

#displaying canvas my_canvas and setting parametres
my_canvas = Canvas(root,bg = "white",height = height_screen , width = width_screen)  

#creating axis for canvas (x1, y1, x2, y2, fill="color") (0 0 -> top left corner)
#rudementary solution, no axis paramtres 
my_canvas.create_line(width_screen/2, 0, width_screen/2, height_screen, fill="black")
my_canvas.create_line(0, height_screen/2, width_screen, height_screen/2, fill="black")

# convert dataframe column to list to be able to iterate 
x_value_list = df[0].tolist()
y_value_list = df[1].tolist()
category_list = df[2].tolist()

#middle of screen
center_x = width_screen/2
center_y = height_screen/2

# x and y position scaler for coordinate of points (ovals)
width_scaler = center_x*0.9
height_scaler = center_y*0.9

#oval size


# create_oval: the top left and bottom right corners of the bounding rectangle for the oval.

# loop that iterates through the length of ther dataset using one of the datasets columns
# through each iteration it checks which of the category string it belongs to and colors it accordingly
# the position of the oval is manipulated using the (...) to be scaled to the acnvas size
for i in range(len(x_value_list)):
    if category_list[i] == "a" or category_list[i] == "foo":
        my_canvas.create_oval(center_x + x_value_list[i]-7, center_y + y_value_list[i]+7, center_x + x_value_list[i]+7, center_y + y_value_list[i]-7, fill="red" )
    if category_list[i] == "b" or category_list[i] == "baz":
        my_canvas.create_oval(center_x + x_value_list[i]-7, center_y + y_value_list[i]+7, center_x + x_value_list[i]+7, center_y + y_value_list[i]-7, fill="green" )
    if category_list[i] == "c" or category_list[i] == "bar":
        my_canvas.create_oval(center_x + x_value_list[i]-7, center_y + y_value_list[i]+7, center_x + x_value_list[i]+7, center_y + y_value_list[i]-7, fill="blue" )


#other stuff for canvas
my_canvas.pack()  
root.mainloop()  

    







