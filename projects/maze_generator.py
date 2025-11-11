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
    turtle.title("Simple Maze Generator")

# DRAW WALL 
def draw_wall(x, y, size):
    """Draws a single square wall cell."""
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()

# GENERATE MAZE
def generate_maze(rows, cols, cell_size):
    """Uses nested loops and conditionals to make a simple maze."""
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

# MARK START & END
def mark_points(rows, cols, cell_size):
    start_x = -cols * cell_size / 2
    start_y = rows * cell_size / 2

    # Start point
    turtle.goto(start_x + 5, start_y - 5)
    turtle.color("green")
    turtle.write("START", font=("Arial", 12, "bold"))

    # End point
    turtle.goto(start_x + (cols - 1) * cell_size + 5, start_y - (rows - 1) * cell_size - 25)
    turtle.color("red")
    turtle.write("END", font=("Arial", 12, "bold"))
    turtle.color("black")

# MAIN FUNCTION
    setup_turtle()
    rows = 6
    cols = 6
    cell_size = 50

    generate_maze(rows, cols, cell_size)
    mark_points(rows, cols, cell_size)

    turtle.done()

# RUN PROGRAM
if __name__ == "__main__":
    main()
