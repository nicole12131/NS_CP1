# Ns 1st 🔨 Maze Generator

import turtle
import random

# Setup the turtle screen
def setup():
    screen = turtle.Screen()
    screen.title("Simple Maze Generator")
    screen.bgcolor("white")
    screen.setup(width=800, height=800)
    turtle.speed(0)
    turtle.pensize(3)
    turtle.hideturtle()

grid_row = [[0,1],[0,0],[1,1],[0,1],[1,0],[0,0],
            [1,0],[0,1],[0,0],[1,1],[1,0],[0,1],
            [0,0],[1,0],[0,1],[1,0],[0,0],[1,0],
            [0,1],[0,0],[1,1],[0,1],[1,0],[0,0],
            [1,0],[0,1],[0,0],[1,1],[1,0],[0,1],
            [0,0],[1,0],[0,1],[1,0],[0,0],[1,0],]
ro
