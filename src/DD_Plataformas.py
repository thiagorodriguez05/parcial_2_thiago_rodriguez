import pygame
from BB_Modificacion_imagenes import obtener_rectangulo


class Plataformas():
    def __init__(self, animacion: None, inicio, tamaño, final) -> None:
        # self.reescalar = reescalar_imagenes(animacion, tamaño[0], tamaño[1])
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
