#importamos las bibliotecas necesarias
import pygame #libreria para juegos 2d en python
import sys #permite salir del programa correctamente.
from vista.personaje_grafico import personajeGrafico
from modelos.Elfo import Elfo
#--------------------------------------#
#agregar los demas modelos
#----------------------------------------#
from control.controlador import controlador

#inicializamos todos los modulos de pygame
pygame.init()

#definimos el tamanio de la ventana (ancho x alto en pixeles)
ANCHO,  ALTO = 800,600
pantalla= pygame.display.set_mode((ANCHO,ALTO)) # crea la ventana

#velocidad = 5 #velocidad de movimiento (en pixeles por cuadro)

#titulo de la ventana
pygame.display.set_caption("Juego Modularizado Grupal")

#definimos constantes de colores en formato RGB (rojo, verde, azul)
NEGRO = (0,0,0) #COLOR DE FONDO
#ROJO = (255,0,0) #RECTANGULO ROJO
#AZUL = (0,0,255) #RECTANGULO AZUL
BLANCO = (255,255,255)

fuente = pygame.font.SysFont(None, 36)


#crear personajes
jugador1 = personajeGrafico(100,100, (255,0,0), Elfo("ELfo",100,150,89,0,0,2,False))
jugador2 = personajeGrafico(300,200,(0,0,255), Elfo ("elfo2",150,87,102,0,0,3,False))

#crear controlador
controlador = controlador(jugador1,jugador2, ANCHO,ALTO)

# creamos un reloj para controlar los cuadros por segundo (FPS)
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    controlador.manejar_eventos()
    #pintamosla pantalla de negro
    pantalla.fill(NEGRO)
    #DIBUJAMOS LOS JUAGADORES EN LA PANTALLA
    jugador1.dibujar(pantalla)
    jugador2.dibujar(pantalla)
    texto1= fuente.render(f"{jugador1.modelo.get_nombre()}:{jugador1.modelo.get_vida()}", True, BLANCO)
    pantalla.blit(texto1, (10,10))
    texto2 = fuente.render(f"{jugador2.modelo.get_nombre()}:{jugador2.modelo.get_vida()}", True, BLANCO)
    pantalla.blit(texto2, (10,40))
    
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()
sys.exit()