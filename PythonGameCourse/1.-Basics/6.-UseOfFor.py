import turtle

s = turtle.Screen()
t = turtle.Turtle()


'''for i in range(4): #dibujat un cuadrado
    t.forward(100)
    t.right(90)
'''
count = 0
while count <= 100:
    t.circle(count)
    count += 10
    
   

turtle.done()