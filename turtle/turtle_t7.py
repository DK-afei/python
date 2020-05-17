import turtle

t7 = turtle.Turtle()

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    t7.pencolor(colors[x % 6])
    t7.width(x  / 100 + 1)
    t7.forward(x)
    t7.left(59)

turtle.done()