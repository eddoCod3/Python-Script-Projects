import turtle

s= turtle.Screen()
t= turtle.Turtle()
s.bgcolor("blue")
s.title("Personalizacion")

t.shapesize(10,5,1) # cambiar tamaño de tortuga, ancho largo, border
t.shapesize(5,10,1)
t.shapesize(3,3,3)
t.fillcolor("green") #Color de la tortuga
t.pencolor("orange") #color de la tinta y borde de la tortuga

t.forward(100)
t.forward(100)

t.color("white","brown") # cambiar color de la tinta y la tortuga

t.pensize(5) #cambiar el tamaño del grosor de la linea

t.left(50)
t.forward(200)

turtle.done()