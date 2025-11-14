# Ns 1st 🔨 Maze Generator

import turtle

# Setup turtle
turtle.speed(0)
turtle.pensize(3)
turtle.hideturtle()
# make maze grid row 
grid_row = [
    [0,1,1,1,1,1],
    [0,0,0,1,0,1],
    [1,1,0,1,0,1],
    [1,0,0,0,0,1],
    [1,0,1,1,1,1],
    [1,0,0,0,0,1],
    [1,1,1,1,1,0]
]
# rows, cols,and cell sizes 
rows = len(grid_row)
cols = len(grid_row[0])
cell_size = 30

# Move to starting position
turtle.penup()
turtle.goto(-cols*cell_size/2, rows*cell_size/2)
turtle.setheading(0)

# Draw based on row data 
for i in range(rows):
    for j in range(cols):
        if grid_row[i][j] == 0:
            turtle.penup()
        else:
            turtle.pendown()
        turtle.forward(cell_size)

    # Finished row and move down to next line
    turtle.penup()
    turtle.backward(cols * cell_size)
    turtle.right(90)
    turtle.forward(cell_size)
    turtle.left(90)

turtle.done()
