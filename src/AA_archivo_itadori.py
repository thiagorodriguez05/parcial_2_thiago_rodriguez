import pygame
from BB_Modificacion_imagenes import girar_imagenes
from CC_Pantalla import H

#                                                          MOVIMIENTOS:

#QUIETO 
personaje_quieto_derecha = [pygame.image.load("assets/img/quieto/0.png"),
                                                pygame.image.load("assets/img/quieto/1.png"),
                                                pygame.image.load("assets/img/quieto/2.png"),
                                                pygame.image.load("assets/img/quieto/3.png"),]
personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)


#CORRE 
personaje_camina_derecha = [pygame.image.load("assets/img/camina_derecha/0.png"),
                                                pygame.image.load("assets/img/camina_derecha/1.png"),
                                                pygame.image.load("assets/img/camina_derecha/2.png"),
                                                pygame.image.load("assets/img/camina_derecha/3.png"),
                                                pygame.image.load("assets/img/camina_derecha/4.png"),
                                                pygame.image.load("assets/img/camina_derecha/5.png"),
                                                pygame.image.load("assets/img/camina_derecha/6.png"),
                                                pygame.image.load("assets/img/camina_derecha/7.png")]
personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)


#SALTA
personaje_salta_derecha = [pygame.image.load("assets/img/salto/1.png"),
                                                pygame.image.load("assets/img/salto/2.png"),
                                                pygame.image.load("assets/img/salto/3.png"),
                                                pygame.image.load("assets/img/salto/4.png")]
personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)


# ATAQUES:
ataque_principal = [pygame.image.load("assets/img/ataque_1/8.png"),
                                                pygame.image.load("assets/img/ataque_1/9.png"),
                                                pygame.image.load("assets/img/ataque_1/10.png"),
                                                pygame.image.load("assets/img/ataque_1/11.png"),
                                                pygame.image.load("assets/img/ataque_1/12.png")]
ataque_principal_izquierda = girar_imagenes(ataque_principal, True, False)


ataque_disparo = [pygame.image.load("assets/img/disparo/0.png"),
                                                    pygame.image.load("assets/img/disparo/1.png"),
                                                    pygame.image.load("assets/img/disparo/2.png"),
                                                    pygame.image.load("assets/img/disparo/3.png"),
                                                    pygame.image.load("assets/img/disparo/4.png"),
                                                    pygame.image.load("assets/img/disparo/5.png"),
                                                    pygame.image.load("assets/img/disparo/6.png"),
                                                    pygame.image.load("assets/img/disparo/7.png"),
                                                    pygame.image.load("assets/img/disparo/8.png"),
                                                    pygame.image.load("assets/img/disparo/9.png")]
ataque_disparo_izquierda = girar_imagenes(ataque_disparo, True, False)


# MUERTE:
personaje_muerte_izquierda = [pygame.image.load("assets/img/muerte/0.png"),
                                            pygame.image.load("assets/img/muerte/1.png"),
                                            pygame.image.load("assets/img/muerte/2.png"),
                                            pygame.image.load("assets/img/muerte/3.png"),
                                            pygame.image.load("assets/img/muerte/4.png"),
                                            pygame.image.load("assets/img/muerte/5.png")]
personaje_muerte_derecha = girar_imagenes(personaje_muerte_izquierda, True, False)

# posiciones, tamaños
posicion_inicial = (H / 2 - 300, 650)
tamaño = (75, 85)


# ACCIONES
diccionario_animaciones = {}
diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecha
diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_animaciones["salta_izquierda"] = personaje_salta_izquierda
diccionario_animaciones["salta_derecha"] = personaje_salta_derecha
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["camina_derecha"] = personaje_camina_derecha
diccionario_animaciones["Muerte_derecha"] = personaje_muerte_derecha
diccionario_animaciones["Muerte_izquierda"] = personaje_muerte_izquierda

diccionario_animaciones["disparo"] = ataque_disparo
diccionario_animaciones["disparo_izquierda"] = ataque_disparo_izquierda

diccionario_animaciones["ataque_patada"] = ataque_principal
diccionario_animaciones["ataque_patada_izquierda"] = ataque_principal_izquierda
