import turtle

color = input('color of background: ')
pensize = input('pensize: ')

wn = turtle.Screen()
# set the window background color
wn.bgcolor(color)

tess = turtle.Turtle()
# make tess blue
tess.color("blue")
# set the width of her pen
tess.pensize(pensize)

tess.forward(50)
tess.left(120)
tess.forward(50)

# wait for a user click on the canvas
wn.exitonclick()
