import turtle

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length / 3)
            turtle.backward(length)
            turtle.right(60)

t = turtle.Turtle
#t.speed(1,1)
t.color("light blue")
t.penup
t.pos(0,0)
t.pendown

def snowflake_drawing():
    for i in range(6):
        draw_branch(100)
        t.right(60)
