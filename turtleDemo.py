import turtle

radius = 100
pen = turtle.Turtle()

# non shaded
for i in range(360):
    pen.forward(1)
    pen.right(1)

# shaded
for i in range(360):
    pen.forward(radius)
    pen.backward(radius)
    pen.right(1)

turtle.done()


