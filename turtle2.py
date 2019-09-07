import turtle

def spiral(sides,trum,color,width):

    t = turtle.Turtle
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(n)
        t.penup()
        t.left(60)
        t.forward(10)
        t.right(60)
        t.pendown()

        t.hideturtle()
spiral(130,60,"cyan",5)
         
