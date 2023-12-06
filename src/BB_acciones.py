from BB_Modificacion_imagenes import reescalar_imagenes

def reescalar_animaciones(animaciones, clave, ancho, alto):
    for clave in animaciones:
        reescalar_imagenes(clave, ancho, alto)


def animar(pantalla, que_animacion, animaciones, contador, lados_main):
    animacion = animaciones[que_animacion]
    largo = len(animacion)
    if contador >= largo:
        contador = 0
    pantalla.blit(animacion[contador], lados_main)
    contador += 1


def mover(velocidad, lados):
    for lado in lados:
        lados[lado].x += velocidad