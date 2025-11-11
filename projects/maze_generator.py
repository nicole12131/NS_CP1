# Ns 1st 🔨 Maze Generator
import turtle
import random

#  SETUP 
def setup_turtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(3)
    turtle.penup()
    turtle.bgcolor("white")
    turtle.title("Maze Generator")

# DRAW WALL 
def draw_wall(x, y, size):
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()

# GENERATE MAZE
def generate_maze(rows, cols, cell_size):
    start_x = -cols * cell_size / 2
    start_y = rows * cell_size / 2

    # Go through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * cell_size
            y = start_y - row * cell_size

            # Leave start and end open
            if (row == 0 and col == 0) or (row == rows - 1 and col == cols - 1):
                continue

            # Randomly decide if this cell is a wall or not
            # More False values mean more open spaces so the maze is solvable
            if random.choice([True, False, False, False]):
                draw_wall(x, y, cell_size)



def set_turtle():
    rows = 6
    cols = 6
    cell_size = 50
    draw_wall(cols, rows, cell_size)
    generate_maze(rows, cols, cell_size)
    
    turtle.done()


set_turtle()
setup_turtle()