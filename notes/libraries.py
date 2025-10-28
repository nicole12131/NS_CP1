# NS 1st Libraries and built in functions notes
import turtle as t 
import random
colors = ["orange", "green", "blue", "purple", "red"]
side = random.randint(10,500)
t.color(random.choice(colors))
t.shape("turtle")

t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50,50)

t.pendown()

t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()

t.done()