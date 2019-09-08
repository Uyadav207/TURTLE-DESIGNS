import turtle
t=turtle.Turtle()
t.color("red")

for side in range(20):
    t.forward(30*side)
    t.left(360/3)
t.hideturtle()