import pygame
from BB_Modificacion_imagenes import girar_imagenes


#CAMINA
boss_camina_derecha = [pygame.image.load("assets/img/enemigos/deidara/moviendo/0.png"),
                            pygame.image.load("assets/img/enemigos/deidara/moviendo/1.png"),
                            pygame.image.load("assets/img/enemigos/deidara/moviendo/2.png"),
                            pygame.image.load("assets/img/enemigos/deidara/moviendo/3.png"),
                            pygame.image.load("assets/img/enemigos/deidara/moviendo/4.png"),
                            pygame.image.load("assets/img/enemigos/deidara/moviendo/5.png"),]
boss_camina_izquierda = girar_imagenes(boss_camina_derecha, True, False)

#ATAQUES
boss_ataque = [pygame.image.load("assets/img/enemigos/deidara/ataque/0.png"), 
                        pygame.image.load("assets/img/enemigos/deidara/ataque/1.png"),]
boss_izquierda = girar_imagenes(boss_ataque, True, False)


#ACCIONES
diccionario_boss = {}
diccionario_boss["Camina_derecha"] = boss_camina_derecha
diccionario_boss["Camina_izquierda"] = boss_camina_izquierda

diccionario_boss["Ataque_derecha"] = boss_ataque
diccionario_boss["Ataque_izquierda"] = boss_izquierda

