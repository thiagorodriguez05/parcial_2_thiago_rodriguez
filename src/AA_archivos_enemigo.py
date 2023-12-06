import pygame
from BB_Modificacion_imagenes import girar_imagenes


#CAMINA
enemigo_derecha = [pygame.image.load("assets/img/enemigos/itachi/18.png"),
                            pygame.image.load("assets/img/enemigos/itachi/19.png"),
                            pygame.image.load("assets/img/enemigos/itachi/20.png"),
                            pygame.image.load("assets/img/enemigos/itachi/21.png"),
                            pygame.image.load("assets/img/enemigos/itachi/22.png"),
                            pygame.image.load("assets/img/enemigos/itachi/23.png")]
enemigo_izquierda = girar_imagenes(enemigo_derecha, True, False)


#EXPLOSION
explosion = [pygame.image.load("assets/img/disparo/9.png"),
                            pygame.image.load("assets/img/disparo/10.png")]
explosion_izquierda = girar_imagenes(explosion, True, False)


#TAMAÑO
Tamaño_enemigo = (100, 90)


#ACCIONES
diccionario_enemigo = {}
diccionario_enemigo["Movimiento_derecha"] = enemigo_derecha        
diccionario_enemigo["movimiento_izquierda"] = enemigo_izquierda     

diccionario_enemigo["explosion"] = explosion    
diccionario_enemigo["explosion_izquierda"] = explosion_izquierda    