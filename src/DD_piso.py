import pygame
from BB_Modificacion_imagenes import obtener_rectangulo


class Plataformas():
    def __init__(self, animacion, inicio, tamaño, final) -> None:
        self.animaciones = pygame.image.load(animacion)
        self.animaciones = pygame.transform.scale(self.animaciones, (tamaño[0], tamaño[1]))
        self.rectangulo_plataforma = self.animaciones.get_rect()
        self.rectangulo_plataforma.x = inicio[0]
        self.rectangulo_plataforma.y = inicio[1]
        self.inicio = inicio
        self.final = final
        self.velocidad = 3
        self.lados = obtener_rectangulo(self.rectangulo_plataforma)
        self.direccion = 1


    def animar(self, pantalla):
        pantalla.blit(self.animaciones, self.lados["main"])


    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad


    def update_movimiento(self, pantalla):
        if self.direccion == 1:
            if self.lados["main"].x < self.final[0]:
                self.animar(pantalla)
                self.mover(self.velocidad)
            else:
                self.animar(pantalla)
                self.direccion = -1  
        else:
            if self.lados["main"].x > self.inicio[0]:
                self.animar(pantalla)
                self.mover(-self.velocidad)  
            else:
                self.animar(pantalla)
                self.direccion = 1 


class Piso:
    def __init__(self, ubicacion_x, ubicacion_y, largo, ancho):
        self.x = ubicacion_x
        self.y = ubicacion_y
        self.largo = largo
        self.ancho = ancho


    def crear_piso(self, pantalla):
        self.piso = pygame.Rect(self.x, self.y, self.largo, self.ancho)
        self.lados = obtener_rectangulo(self.piso)
        pygame.draw.rect(pantalla, (255, 0, 0), self.piso)


    def daño_personaje(self, personaje):
        self.piso = pygame.Rect(self.x, self.y, self.largo, self.ancho)
        self.lados = obtener_rectangulo(self.piso)
        if self.piso.colliderect(personaje.lados["main"]):
            personaje.vidas -= 3


