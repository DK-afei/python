import turtle
import random

t8 = turtle.Turtle()

for n in range(60):
    t8.penup()
    t8.goto(random.randint(-400, 400), random.randint(-400, 400))
    t8.pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    t8.pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    t8.pensize(random.randint(1, 5))

    for i in range(6):
        t8.circle(circle_size)
        t8.left(60)

turtle.done()