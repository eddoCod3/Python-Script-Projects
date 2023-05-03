import turtle
import random

s= turtle.Screen()
s.title("Turtle-Race")
s.bgcolor("gray")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

def personalize__Player(color,icon,sizeofpen,sizeoftheplayer,playername):
    playername.shape(icon)
    playername.color(color,color)
    playername.shapesize(sizeoftheplayer,sizeoftheplayer,sizeoftheplayer)
    playername.pensize(sizeofpen)

def draw_goal(posx,posy,sizeofGoal,player):
    player.penup()
    player.goto(posx,posy) #200,200
    player.pendown()
    player.circle(sizeofGoal) #40
    
    


jugador1.hideturtle()
personalize__Player("green", "turtle", 3, 2,jugador1)


jugador2.hideturtle()
personalize__Player("blue", "turtle", 3, 2,jugador2)

draw_goal(200, 200, 40, jugador1)


jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()


draw_goal(200, -200, 40, jugador2)

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()


dado = [1,2,3,4,5,6]
counter = 0
for counter in range(20):
    if jugador1.pos() >=(200,200):
        print("El jugador 1 ya gano")
        break
    elif jugador2.pos() >=(200,-200):
        print("El jugador 2 ya gano")
        break
    else:
        turno1 =input("Presiona la tecla enter para avanzar")
        turno1 = random.choice(dado) 
        print("Tu numero es :",turno1,"\n Avanzas:  ",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 =input("Presiona la tecla shift para avanzar")
        turno2 = random.choice(dado) 
        print("Tu numero es :",turno2,"\n Avanzas:  ",turno1*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

turtle.done()