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


# Draw one cell of the maze
def draw_cell(x, y, size, walls):
    turtle.penup()

    # North wall
    if "N" in walls:
        turtle.goto(x, y)
        turtle.setheading(0)  # face east
        turtle.pendown()
        turtle.forward(size)
        turtle.penup()

    # East wall
    if "E" in walls:
        turtle.goto(x + size, y)
        turtle.setheading(-90)  # face south
        turtle.pendown()
        turtle.forward(size)
        turtle.penup()

    # South wall
    if "S" in walls:
        turtle.goto(x + size, y - size)
        turtle.setheading(180)  # face west
        turtle.pendown()
        turtle.forward(size)
        turtle.penup()

    # West wall
    if "W" in walls:
        turtle.goto(x, y - size)
        turtle.setheading(90)  # face north
        turtle.pendown()
        turtle.forward(size)
        turtle.penup()

# Generate maze layout
def generate_maze(rows, cols):
    maze = [[set(["N", "E", "S", "W"]) for _ in range(cols)] for _ in range(rows)]
    visited = set()

    def carve(r, c):
        visited.add((r, c))
        directions = [("N", -1, 0), ("S", 1, 0), ("E", 0, 1), ("W", 0, -1)]
        random.shuffle(directions)

        for d, dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # remove walls between cells
                maze[r][c].discard(d)
                if d == "N":
                    maze[nr][nc].discard("S")
                if d == "S":
                    maze[nr][nc].discard("N")
                if d == "E":
                    maze[nr][nc].discard("W")
                if d == "W":
                    maze[nr][nc].discard("E")
                carve(nr, nc)

    carve(0, 0)
    return maze

# Draw the maze grid
def draw_maze(maze, size):
    start_x, start_y = -200, 200
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            x = start_x + c * size
            y = start_y - r * size
            draw_cell(x, y, size, maze[r][c])


# Mark start and end points
def mark_points(size, rows, cols):
    start_x, start_y = -200, 200
    turtle.penup()
    # Start point 
    turtle.goto(start_x + size / 2, start_y - size / 2)
    turtle.dot(25, "green")
    # End point
    turtle.goto(start_x + (cols - 1) * size + size / 2,
                start_y - (rows - 1) * size - size / 2)
    turtle.dot(25, "red")


# Main program

def main():
    setup()
    rows, cols = 6, 6 
    size = 60
    maze = generate_maze(rows, cols)
    draw_maze(maze, size)
    mark_points(size, rows, cols)
    turtle.done()

# Run the program
if __name__ == "__main__":
    main()
