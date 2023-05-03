import turtle

s = turtle.Screen()
t= turtle.Turtle()

t.speed(10) #acepta valores del 1 al 10, uno el mas lento 10 es el mas rapido
t.circle(10)
t.speed(10)
t.circle(30)

t.dot(30) #tamaño del punto 

t.hideturtle() #ocultar a la tortuga
t.speed(1)
t.circle(40)
t.showturtle() # mostrat a la tortuga
t.circle(100)

t.setx(100)
t.sety(-500)
turtle.done()