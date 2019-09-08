import turtle  
star = turtle.Turtle() 
  
for i in range(10): 
    star.forward(50) 
    star.right(144)
for j in range(10):
    star.backward(50)
    star.left(144)
for m in range(2):
     star.backward(50)
     star.right(360)
for k in range(10):
    star.forward(50)
    star.right(144)
      
turtle.done() 