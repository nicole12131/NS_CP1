# Ns 1st 🔨 Maze Generator

import turtle

# set up turtle
def setup():
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    t.pensize(3)
    t.hideturtle()



grid_row = [[0,1,1,1,1,1],
            [0,0,0,1,0,1],
            [1,1,0,1,0,1],
            [1,0,0,0,0,1],
            [1,0,1,1,1,1],
            [1,0,0,0,0,1],
            [1,1,1,1,1,0]]

grid_column = [[0,1,1,1,1,1],
            [0,0,0,1,0,1],
            [1,1,0,1,0,1],
            [1,0,0,0,0,1],
            [1,0,1,1,1,1],
            [1,0,0,0,0,1],
            [1,1,1,1,1,0]]

row = 6
columns = 6
cell_size = 30

for i in range(row):
    for j in range(columns):
        if grid_row[j][i] == 0:
            turtle.penup()
            turtle.forward(cell_size)
        if grid_row[j][i] == 1:
            turtle.pendown()
            turtle.forward(cell_size)

turtle.hideturtle

turtle.done()




