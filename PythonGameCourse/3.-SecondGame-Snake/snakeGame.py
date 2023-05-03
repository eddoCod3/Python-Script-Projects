import turtle
import time
import random

s= turtle.Screen()
s.setup(600,600)
s.bgcolor("gray")
s.title("Snake")

delay = 0.05
marcador = 0
marcador_alto = 0
snakePlayer= turtle.Turtle()
def personalize__Player(color,icon,sizeofpen,sizeoftheplayer,playername):
    playername.shape(icon)
    playername.color(color,color)
    playername.shapesize(sizeoftheplayer,sizeoftheplayer,sizeoftheplayer)
    playername.pensize(sizeofpen)


comida = turtle.Turtle()
personalize__Player("orange", "circle", 1, 1, comida)
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo =[]
texto = turtle.Turtle()
texto.speed(0)
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador:0\tMarcador mas alto:0", align = "center", font=("verdana",24,"normal"))
def arriba():
    snakePlayer.direction = "up"
def abajo():
    snakePlayer.direction ="down"
def izquierda ():
    snakePlayer.direction = "left"
def derecha ():
    snakePlayer.direction = "right"
def movement ():
    if snakePlayer.direction =="up":
        y = snakePlayer.ycor()
        snakePlayer.sety(y+20)
    elif snakePlayer.direction =="down":
        y = snakePlayer.ycor()
        snakePlayer.sety(y-20)
    elif snakePlayer.direction =="right":
        z= snakePlayer.xcor()
        snakePlayer.setx(z+20)
    elif snakePlayer.direction =="left":
        z= snakePlayer.xcor()
        snakePlayer.setx(z-20)
    pass

personalize__Player("green", "square", 1, 1, snakePlayer)


snakePlayer.penup()
snakePlayer.goto(0,0)
snakePlayer.direction ="stop"

s.listen()
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(izquierda,"Left")
s.onkeypress(derecha,"Right")

while True:
    s.update()

    if snakePlayer.xcor() > 300  or snakePlayer.xcor() < -300 or  snakePlayer.ycor() > 300 or snakePlayer.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        snakePlayer.home()
        snakePlayer.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador, marcador_alto), align="center", font=("verdana",24,"normal"))   



    if snakePlayer.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        new_body.goto(0,100)
        new_body.speed(0)
        cuerpo.append(new_body)

        marcador +=10

        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador, marcador_alto), align="center", font=("verdana",24,"normal"))

       
    total = len(cuerpo)
    for index in range(total -1,0,-1):
     x = cuerpo[index-1].xcor()
     y = cuerpo[index-1].ycor()
     cuerpo[index].goto(x,y)

     if total > 0:
        x = snakePlayer.xcor()
        y = snakePlayer.ycor()
        cuerpo[0].goto(x,y)    
        
    movement()

    for i in cuerpo:
        if i.distance(snakePlayer) <20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            snakePlayer.home()
            cuerpo.clear()
            snakePlayer.direction = "stop"
            pass
    time.sleep(delay)

turtle.done()