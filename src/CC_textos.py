import pygame

pygame.font.init()
color_blanco = (255, 255, 255)

def crear_texto(pantalla, texto, posicion, color, tamaño):
    Formato = pygame.font.Font(None, tamaño)
    texto = Formato.render(texto, True, color)
    pantalla.blit(texto, posicion)



