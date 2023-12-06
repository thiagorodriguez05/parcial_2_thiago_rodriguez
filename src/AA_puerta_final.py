import pygame
from BB_Modificacion_imagenes import reescalar_imagenes, obtener_rectangulo


animacion_puerta_desbloqueada = [pygame.image.load("assets\img\objetos\puerta_abierta.png")]
animacion_puerta_bloqueada = [pygame.image.load("assets\img\objetos\puerta_cerrada.png")]

diccionario_puerta = {}
diccionario_puerta["Desbloqueada"] = animacion_puerta_desbloqueada
diccionario_puerta["Bloqueada"] = animacion_puerta_bloqueada

class Puerta:
    def __init__(self, animacion, ubicacion) -> None:
        self.animaciones = animacion
        self.reescalar = self.reescalar_animaciones()
        self.rectangulo = self.animaciones["Desbloqueada"][0].get_rect()
        self.rectangulo.x = ubicacion[0]
        self.rectangulo.y = ubicacion[1]
        self.contador_pasos = 0
        self.lados = obtener_rectangulo(self.rectangulo)


    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], 114, 136)


    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1


    def finalizar_nivel(self, pantalla, personaje):
        if self.lados["main"].colliderect(personaje.lados["main"]):
            print("Salio")
            


    def update(self, pantalla, personaje):
        if personaje.llaves_obtenidas > 0:
            self.animar(pantalla, "Desbloqueada")
            self.finalizar_nivel(pantalla, personaje)
        else:
            self.animar(pantalla, "Bloqueada")

puerta_nivel_uno = Puerta(diccionario_puerta, (1353, 603))


