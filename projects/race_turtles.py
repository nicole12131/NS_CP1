# NS 1st 🔨 Turtle Race
import turtle
import random
import time

# setup the screen
def setup_screen():
    screen = turtle.Screen()
    screen.title("🐢 Turtle Race 🐢")
    screen.bgcolor("lightblue")

    # draw finish line
    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.color("black")
    line.penup()
    line.goto(250, 200)
    line.pendown()
    line.right(90)
    for i in range(20):
        line.forward(10)
        line.penup()
        line.forward(10)
        line.pendown()
    return screen

# make turtles
def create_turtles():
    colors = ["red", "blue", "green", "orange", "purple"]
    turtles = []
    y_pos = 100

    for color in colors:
        t = turtle.Turtle(shape="turtle")
        t.color(color)
        t.penup()
        t.goto(-250, y_pos)
        t.pendown()
        turtles.append(t)
        y_pos -= 50

    return turtles

# the actual race
def race(turtles):
    finish_line = 250
    winner = None

    while not winner:
        for t in turtles:
            step = random.randint(1, 10)
            t.forward(step)
            if t.xcor() >= finish_line:
                winner = t.color()[0]
                break
        time.sleep(0.05)  # slows down the race a bit
    return winner

# main function
def main():
    screen = setup_screen()
    racers = create_turtles()
    winner = race(racers)

    # show winner message
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, -200)
    msg.write(f"The {winner} turtle won!", align="center", font=("Arial", 18, "bold"))

    print(f"The {winner} turtle won!")  # print in terminal too

    screen.mainloop()

# run the program
if __name__ == "__main__":
    main()