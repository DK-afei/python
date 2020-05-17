import turtle
turtle.screensize(800,600,"green")
turtle.width(10)
turtle.color('blue')


t = turtle.Turtle()
t.shape("turtle")

# for angle in range(0,360,15):
#     t.setheading(angle)
#     t.fd(100)
#     t.write(str(angle) + '°')
#     t.bk(100)
#
# t.reset()
#
# for hour in range(1,13,1):
#     t.setheading(hour*30)
#     t.fd(100)
#     t.write(str(hour)+'.')
#     t.bk(100)

# for i in range(10):
#     t.forward(100)
#     t.left(90)
#     t.forward(10)
#     t.left(90)
#     t. forward(100)
#     t. right(90)
#     t.forward(10)
#     t.right(90)
#
# for i in range(30):
#     t.undo()

# t.home()

t.fd(100)
t.penup()
t.bk(200)
t.pendown()
t.fd(100)
for i in range(3):
    t.undo()

turtle.done()