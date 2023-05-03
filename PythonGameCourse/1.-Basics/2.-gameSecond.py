import turtle

s =turtle.Screen()
t= turtle.Turtle()

t.goto(100,100) #Forma para decirle a la tortuga donde ir
t.goto(-100,100)
t.goto(0,0) #tambien se puede poner t.home()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.done()