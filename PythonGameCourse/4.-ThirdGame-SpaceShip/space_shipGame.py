import pygame
from enemy import enemy
from fire import fire 

#Dimension de la ventana
ANCHO = 800
LARGO = 600
FPS = 60

NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

consolas = pygame.font.match_font("consolas")
Times = pygame.font.match_font("times")
arial = pygame.font.match_font("arial")
courier = pygame.font.match_font("courier")



#clase del jugador
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #cargamos la imagen
        self.image = pygame.image.load("nave.png")
        #selecionamos el rectangulo del sprite
        self.rect = self.image.get_rect()
        #centrar el rectangulo del sprite
        self.rect.center = (400,550)
        #asignamos velocidad
        self.velocidad_x=0
        self.velocidad_y=0


    def update(self):
        #Asignar velocidad cada vez que se cumple el ciclo
        self.velocidad_x=0
        self.velocidad_y=0

        #Variable para captar las pulsaciones del teclado
        teclas = pygame.key.get_pressed()

        #Movimeinto a la izquerda
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        if teclas[pygame.K_SPACE]:
            self.disparo()
            

        #Actualizamos la posicion del peronaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Limitante de los border

        #Border izquierdo y derecho
        if self.rect.left <0 :
            self.rect.left =0
        if self.rect.right >ANCHO:
            self.rect.right = ANCHO
        #Border de arriba y abajo
        if self.rect.bottom > LARGO:
            self.rect.bottom = LARGO
        if self.rect.top < 0:
            self.rect.top = 0
    def disparo(self):
        bala = fire(self.rect.center,self.rect.centery)
        Balas.add(bala)
        laser.play()  
        

    









#Inicio del gameLoop
class inicio():
    pygame.init()


laser = pygame.mixer.Sound("Fire 5.mp3")

#Dibujamos la pantalla del juego
pantalla = pygame.display.set_mode((ANCHO,LARGO))

#Fondo del juego
fondo = pygame.transform.scale(pygame.image.load("Fondo.png").convert(),(1000,600))

#Titulo de la ventana
pygame.display.set_caption("Space Shooter")

#Establece FPS
clock = pygame.time.Clock()

#sprites

jugador = pygame.sprite.Group()
Enemigos = pygame.sprite.Group()
Balas = pygame.sprite.Group()
#Añadir sprites

jugadores = player()
jugador.add(jugadores)

def texto(pantalla,fuente,texto, color,dimesiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimesiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center =(x,y)
    pantalla.blit(superficie,rectangulo)


#Ciclo del videojuego
ejecutando = True

#Ciclo de ejecucion del videojuego
while ejecutando:
    clock.tick(FPS)
    pantalla.blit(fondo, (0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            ejecutando = False

    puntuacion = 0
    texto(pantalla, arial , str(puntuacion) , BLANCO, 50, 700, 50)
    #Actuallizacion de sprites
    jugador.update()
    Enemigos.update()
    Balas.update()

    colison_nave = pygame.sprite.groupcollide(Enemigos,jugador, False,False)

    Colision_bala = pygame.sprite.groupcollide(Enemigos,Balas,True,True)

    if colison_nave:
        puntuacion -= 10 
    if puntuacion < 0:
        puntuacion = 0
        break
    if Colision_bala:
        puntuacion += 30

        
       


    if not Enemigos:
        for x in range(5):
            enemigos = enemy()
            Enemigos.add(enemigos)


    jugador.draw(pantalla)
    Enemigos.draw(pantalla)
    Balas.draw(pantalla)

    pygame.display.flip()