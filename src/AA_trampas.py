import pygame
from BB_Modificacion_imagenes import obtener_rectangulo, reescalar_imagenes


lista_trampa = [pygame.image.load("assets/img/objetos/trampa.png")]

diccionario_trampa = {}
diccionario_trampa["trampa"] = lista_trampa 

class Trampas():
    def __init__(self, inicio, final, tamaño) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.animaciones = diccionario_trampa
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["trampa"][0].get_rect()
        self.rectangulo.x = inicio[0]
        self.rectangulo.y = inicio[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        self.posion_inicial = inicio
        self.posion_final = final
        self.direccion = 1
        self.velocidad = 3

        self.tiempo_invulnerable = 0
        self.tiempo_invulnerable_total = 60

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.ancho, self.alto)
    

    def animar(self, pantalla):
        # pantalla.blit(self.animaciones, self.lados["main"])
        imagen_actual = self.animaciones["trampa"][0]  # Aquí asumo que quieres mostrar la primera imagen de la animación
        pantalla.blit(imagen_actual, self.lados["main"])
        
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].y += velocidad

    def daños_personaje(self, personaje):
        if self.tiempo_invulnerable > 0:
            self.tiempo_invulnerable -= 1

        if self.tiempo_invulnerable == 0:  
            if self.lados["main"].colliderect(personaje.lados["main"]):
                personaje.vidas -= 1
                personaje.puntos -= 15
                self.sonido_vidas = pygame.mixer.Sound("assets\sound\Menos_vida.wav")
                self.sonido_vidas.play()
                self.tiempo_invulnerable = self.tiempo_invulnerable_total
            self.tiempo_invulnerable = self.tiempo_invulnerable_total

    def update(self, pantalla, personaje):
        if self.direccion == 1:
            if self.lados["main"].y < self.posion_final[1]:
                self.animar(pantalla)
                self.mover(self.velocidad)
            else:
                self.animar(pantalla)
                self.direccion = -1  
        else:
            if self.lados["main"].y > self.posion_inicial[1]:
                self.animar(pantalla)
                self.mover(-self.velocidad)  
            else:
                self.animar(pantalla)
                self.direccion = 1 
        self.daños_personaje(personaje)


trampa_uno = Trampas((1292, 72), (1287, 364), (80,80))
listas_trampas = [trampa_uno]

lista_lados_trampas =  [trampa_uno.lados]