import pygame
from BB_Modificacion_imagenes import obtener_rectangulo, reescalar_imagenes

class enemigo():
    def __init__(self, inicio, final, animaciones, tamaño, vidas):
        self.vidas = vidas
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.desplazamiento_y = 0
        
        # animacion:
        self.contador_pasos = 0
        self.acciones = "Movimiento_derecha"
        self.acciones = "explosion"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        # Hitbot
        rectangulo = self.animaciones["Movimiento_derecha"][0].get_rect()
        rectangulo.x = inicio[0]
        rectangulo.y = inicio[1]
        self.lados = obtener_rectangulo(rectangulo)
        self.velocidad = 5
        self.movimiento_inicio = inicio
        self.movimiento_final = final
        self.direccion = 1   
        self.tiempo_daños = 0
        self.tiempo_daños_total = 10
        self.eliminado = False


    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.ancho, self.alto)


    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        if not self.eliminado:  # Verificar si el enemigo ha sido eliminado
            pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        
        self.contador_pasos += 1


    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad


    def update(self, pantalla, lista_plataformas, lista_proyectiles, personaje, lista_enemigos):
        if self.direccion == 1:
            if self.lados["main"].x < self.movimiento_final[0]:
                self.animar(pantalla, "Movimiento_derecha")
                self.mover(self.velocidad)
            else:
                self.animar(pantalla, "Movimiento_derecha")
                self.direccion = -1  
        
        else:
            if self.lados["main"].x > self.movimiento_inicio[0]:
                self.animar(pantalla, "movimiento_izquierda")
                self.mover(-self.velocidad)  
            else:
                self.animar(pantalla, "movimiento_izquierda")
                self.direccion = 1 
        
        self.daños(lista_proyectiles, personaje, lista_enemigos, pantalla)
        self.aplicar_gravedad(lista_plataformas)


    def aplicar_gravedad(self, lista_plataformas):
        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y
        
        if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad
        
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma):
                self.lados["main"].bottom = plataforma.top + 5
                self.desplazamiento_y = 0
                self.esta_saltando = False


    def daños(self, lista_proyectiles, personaje, lista, pantalla):
        if self.tiempo_daños > 0:
            self.tiempo_daños -= 1
        if self.tiempo_daños == 0:
            for proyectil in lista_proyectiles:
                if self.lados["main"].colliderect(proyectil.rectangulo):
                    print("Colision enemigo")
                    self.vidas -= proyectil.daño
                    personaje.puntos += 5
                    lista_proyectiles.remove(proyectil)
                    self.animar(pantalla, "explosion")
            self.tiempo_daños = self.tiempo_daños_total
        
        if self.vidas == 0 and not self.eliminado:
            self.eliminado = True
            personaje.puntos += 10
            self.muerte = pygame.mixer.Sound("assets\sound\muerte.wav")
            self.muerte .play() 
            lista.remove(self)
            print("Chau enemigo")




