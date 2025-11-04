# Ns 1st 🔨 Maze Generator
# import turtle and random 
import turtle 
import random 

# Setup the screen 
def setup_screen():
    wn = turtle.Screen()
    wn.title("Simple Maze Generator")
    wn.bgcolor("white")
    turtle.speed(0)
    turtle.pensize(3)
    turtle.hideturtle()

def draw_cell(x, y, size, walls):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# top
    if walls["top"]:
        turtle.setheading(0)
        turtle.forward(size)
    turtle.penup()
    turtle.goto(x + size, y)
    turtle.pendown()

# right
    if walls["right"]:
        turtle.setheading(-90)
        turtle.forward(size)
    turtle.penup()
    turtle.goto(x + size, y - size)
    turtle.pendown()

# bottom
    if walls["bottom"]:
        turtle.setheading(180)
        turtle.forward(size)
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.pendown()

     # left
    if walls["left"]:
        turtle.setheading(90)
        turtle.forward(size)

# Make the maze layout
def make_maze(rows, cols):
    maze = []
    for r in range(rows):
        row = []
        for c in range(cols):
            walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
            }
# Randomly open some walls to make paths
    if random.random() > 0.5:
        walls["right"] = False
    if random.random() > 0.5:
        walls["bottom"] = False

# Keep borders closed
    if r == 0:
        walls["top"] = True
    if c == 0:
        walls["left"] = True
    if r == rows - 1:
        walls["bottom"] = True
    if c == cols - 1:
        walls["right"] = True

        row.append(walls)
        maze.append(row)
    return maze

# Draw the maze
def draw_maze(maze, size):
    start_x = -150
    start_y = 150
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            x = start_x + c * size
            y = start_y - r * size
            draw_cell(x, y, size, maze[r][c])

# Mark start and end
def mark_points():
    turtle.penup()
    turtle.goto(-150, 160)
    turtle.color("green")
    turtle.write("START", font=("Arial", 10, "bold"))
    turtle.goto(150, -220)
    turtle.color("red")
    turtle.write("END", font=("Arial", 10, "bold"))

#  Main program 
def main():
    setup_screen()
    maze = make_maze(6, 6)
    draw_maze(maze, 50)
    mark_points()
    turtle.done()

main()
