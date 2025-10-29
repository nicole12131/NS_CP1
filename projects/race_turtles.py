# NS 1st 🔨 Turtle Race
import turtle as t
import random as r

screen = t.Screen()
screen.title("Turtle Race")
side = r.randint(100,500)

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()

turtles =[t1, t2, t3, t4, t5]

t1.color("red")
t1.shape("turtle")
t1.setposition(0,0)
t1.speed(r.randint(1,10))
t1.pendown()

t2.color("blue")
t2.shape("turtle")
t2.setposition(1,0)
t2.speed(r.randint(1,9))
t2.pendown()

t3.color("purple")
t3.shape("turtle")
t3.setposition(2,0)
t3.speed(r.randint(1,8))
t3.pendown()

t4.color("green")
t4.shape("turtle")
t4.setposition(3,0)
t4.speed(r.randint(1,7))
t4.pendown()

t5.color("orange")
t5.shape("turtle")
t5.setposition(4,0)
t5.speed(r.randint(1,6))
t5.pendown()

for x in range(1,4):
    t1.forward(side)
    t2.forward(side)
    t3.forward(side)
    t4.forward(side)
    t5.forward(side)