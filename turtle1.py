import turtle
t=turtle.Turtle()
t.color("red")
n=int(input("enter the no."))
for side in range(n):
    t.forward(30*side)
    t.left(360/3)
t.hideturtle()