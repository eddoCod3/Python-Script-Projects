import random
import pygame

ANCHO = 800
LARGO = 600

class enemy(pygame.sprite.Sprite):
    def __init__(self):
           #Heredar la variable de la clase sprite

        super().__init__()

        #Cargar la imagen del enemigo

        self.image = pygame.image.load("ufo.png")

        #obtener el rectangulo de la imagen

        self.rect = self.image.get_rect()

        #Posicion en el mapa

        self.rect.center = (200,500)
        
        #Aparicion Aleatoria


        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)

        #Movimiento del personaje

        self.velocidad_x = random.randrange(1,8)
        self.velocidad_y = random.randrange(1,8)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.left < 0:
            self.velocidad_x += 1
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        if self.rect.top < 0:
            self.velocidad_y += 1
        if self.rect.bottom > LARGO:
            self.velocidad_y -= 1

 
