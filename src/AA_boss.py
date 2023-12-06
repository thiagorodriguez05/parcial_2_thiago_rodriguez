import pygame
from AA_archivos_boss import diccionario_boss
from BB_Modificacion_imagenes import obtener_rectangulo, reescalar_imagenes
from CC_Vida import vidas_jefe


class Jefe:
    def __init__(self, posicion_inicial, posicion_final ) -> None:
        self.gravedad = 1
        self.limite_velocidad_caida = 15
        self.desplazamiento_y = 0
        
        self.vidas = 5
        self.ancho = 130
        self.alto = 180
        
        self.contador_pasos = 0
        self.que_hace = diccionario_boss["Camina_derecha"]
        self.animaciones = diccionario_boss
        self.reescalar_animaciones()
        
        self.rectangulo = self.animaciones["Camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        
        self.inicio = posicion_inicial
        self.final = posicion_final
        
        self.velocidad = 5
        
        self.bandera_derecha = True
        self.direccion = 1
        
        # Velocidades:
        self.tiempo_normal = 0
        self.tiempo_aum_velocidad = 60
        
        self.tiempo_velocidad = 0
        self.tiempo_normalidad = 40
        
        # Ataques:
        self.tiempo_ataque = 0
        self.tiempo_ataque_total = 50
        
        self.tiempo_daños = 0
        self.tiempo_daños_total = 30
        self.activo = True


    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.ancho, self.alto)


    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1


    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad


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


    def update(self, pantalla, personaje, lista_plataformas, lista_enemigos, lista_proyectiles ):
        if self.tiempo_ataque > 0:
            self.tiempo_ataque -= 1
        if self.activo:
            if self.vidas > 0:
                
                if self.direccion == 1:
                    if self.lados["main"].x < self.final[0]:
                        self.animar(pantalla, "Camina_derecha")
                        self.mover(self.velocidad)
                    else:
                        self.animar(pantalla, "Camina_derecha")
                        self.direccion = -1
                elif self.direccion == -1:
                    if self.lados["main"].x > self.inicio[0]:
                        self.animar(pantalla, "Camina_izquierda")
                        self.mover(-self.velocidad)
                    else:
                        self.animar(pantalla, "Camina_izquierda")
                        self.direccion = 1
                elif self.balas != 0 and self.que_hace == "Ataque_derecha":
                    if self.bandera_derecha == True:
                        if not self.esta_saltando:
                            self.disparo()
                            self.animar(pantalla, "Ataque_derecha")
                    elif self.bandera_izquierda == True:
                        if not self.esta_saltando:
                            self.disparo()
                            self.animar(pantalla, "Ataque_izquierda")
                
                self.daño_personaje(pantalla, personaje)
                self.aplicar_gravedad(lista_plataformas)
                self.velocidades()  
                self.daños(lista_proyectiles, personaje)
        
        elif self.vidas < 0: 
            lista_jefe.remove(self) #DESCOMENTAR 
            personaje.puntos += 30
            print("murio el boss")
        vidas_jefe(pantalla, self.vidas)


    def velocidades(self):
        if self.tiempo_normal > 0:
            self.tiempo_normal -= 1
        if self.tiempo_normal == 0:
            self.velocidad = 15
            self.tiempo_normal = self.tiempo_aum_velocidad
        else:
            if self.tiempo_velocidad > 0:
                self.tiempo_velocidad -=1
            if self.tiempo_velocidad == 0:
                self.tiempo_velocidad = self.tiempo_normalidad
                self.velocidad = 5


    def daños(self, lista_proyectiles, personaje):
        if self.tiempo_daños > 0:
            self.tiempo_daños -= 1
        if self.tiempo_daños == 0:
            for proyectil in lista_proyectiles:
                if self.lados["main"].colliderect(proyectil.rectangulo):
                    print(f"Vidas:{self.vidas}")
                    personaje.puntos += 15
                    self.vidas -= 1
                    lista_proyectiles.remove(proyectil)
            self.tiempo_daños = self.tiempo_daños_total
        if self.vidas == 0:
            self.activo = False


    def daño_personaje(self, pantalla, personaje):
        if self.tiempo_ataque == 0 and self.lados["main"].colliderect(personaje.lados["main"]):
            print("el boss ataco")
            self.animar(pantalla, "Ataque_derecha")
            personaje.puntos -= 20
            personaje.vidas -= 1
            self.ataque = pygame.mixer.Sound("assets\sound\Menos_vida.wav")
            self.ataque.play
            self.mover(0)
            self.tiempo_ataque = self.tiempo_ataque_total 
        

boss = Jefe((307, 451), (700, 450))

lista_jefe = [boss]

