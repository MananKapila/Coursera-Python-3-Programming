import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
# this is new
tess.up()
# start with size = 5 and grow by 2
for _ in range(30):
    # leave an impression on the canvas
    tess.stamp()
    # move tess along
    tess.forward(dist)
    # and turn her
    tess.right(24)
    dist = dist + 2
wn.exitonclick()