# Ns 1st 🔨 Maze Generator

import turtle

# setup
def setup():
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)
    t.hideturtle()
    return t

#  draw one wall square 
def draw_wall(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_maze(t, maze, size):
    y = 100  # starting Y position
    for row in maze:
        x = -100  # starting X position
        for cell in row:
            if cell == 1:
                draw_wall(t, x, y, size)
            x += size  # move to next column
        y -= size  # move to next row

# main program
def main():
    t = setup()
maze = [
        [1,1,1,1,1,1],
        [0,0,0,1,0,1],
        [1,1,0,1,0,1],
        [1,0,0,0,0,1],
        [1,0,1,1,1,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,1]
    ]

    draw_maze(t, maze, 30)
    t.penup()
    t.goto(-90, 100)
    t.write("START", font=("Arial", 10, "bold"))
    t.goto(60, -90)
    t.write("END", 
font=("Arial", 10, "bold"))
    turtle.done()

main()
