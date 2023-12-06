import pygame
from BB_Modificacion_imagenes import obtener_rectangulo
from CC_Pantalla import*


######################################################################################################################



class Proyectil:
    def __init__(self, x, y, direccion, animacion, daño, velocidad):
        self.x = x
        self.y = y
        self.direccion = direccion
        
        self.velocidad = velocidad
        self.daño = daño
        self.animaciones = animacion
        
        self.animaciones = pygame.image.load(self.animaciones)
        self.imagen_redimensionada = pygame.transform.scale(self.animaciones, (40, 40))
        
        self.rectangulo = self.imagen_redimensionada.get_rect()
        self.rectangulo.x = self.x  
        self.rectangulo.y = self.y  
        
        self.lados_disparo = obtener_rectangulo(self.rectangulo)
        
        self.tiempo_personaje = 0
        self.tiempo_personaje_total = 5


    def mover(self, mi_personaje):
        self.x += self.velocidad * self.direccion
        self.rectangulo.move_ip(self.velocidad * self.direccion, 0)  # Actualizar posición del rectángulo de colisión
        if self.x < 0 or self.x > W:
            # Eliminar el proyectil de la lista de proyectiles
            mi_personaje.lista_proyectil.remove(self)


    def dibujar(self, pantalla):
        pantalla.blit(self.imagen_redimensionada, (self.x, self.y))


    def update(self, pantalla,  lista_personaje):
        self.dibujar(pantalla)
        self.mover(lista_personaje)







