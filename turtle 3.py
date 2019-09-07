import turtle
t=turtle.Turtle()
t.color("red")

for side in range(50):
    t.forward(30*side)
    t.backward(20*side)
    t.left(360/4)
t.hideturtle()