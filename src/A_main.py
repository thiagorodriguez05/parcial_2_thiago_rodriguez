import pygame
import sys
from ZZ_inicio import Inicio
from CC_Pantalla import*


RELOJ = pygame.time.Clock()
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)

pygame.init()

pygame.display.set_caption("Jujutsu Kaisen")
icono = pygame.image.load("assets/img/pantalla/logo.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("assets/img/pantalla/fondo.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)


formulario = Inicio(pantalla,497, 397,  450, 300, True, "assets/img/pantalla/nada.png")


while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN: #toco la pantalla
            print(evento.pos)
    keys = pygame.key.get_pressed()


    pantalla.blit(fondo, (0, 0))  
    formulario.update(eventos) 
    pygame.display.update()
