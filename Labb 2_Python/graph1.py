import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
import turtle

def MAX(sets):
    return (max(sets))

# Put the code in a function so you cal call it later
def display_graph(data):

    df = pd.read_csv(data)

 #   x = []
  #  y = []
  #  color = []

    playground = turtle.Screen()       # use nouns for objects, play is a verb

    playground.bgcolor("white")
    playground.screensize(500, 55)
    playground.title("Scatter Plot")

    for a in range(len(df)):
        kord = turtle.Turtle()

        kord.penup()

        kord.setposition(df[a][0], df[1][a])

        if df[a][2] == ("foo") or ("a"):
             kord.color("blue")
        elif df[a][2] == ("baz") or ("b"):
             kord.color("red")
        elif df[a][2] == ("bar") or ("c"):
             kord.color("green")
        else:
             kord.color("black")

        kord.stamp()

