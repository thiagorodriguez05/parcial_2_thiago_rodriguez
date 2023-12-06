from BB_Modificacion_imagenes import obtener_rectangulo, reescalar_imagenes

class Elementos ():
    def __init__(self, animacion, posiciones, tamaño) -> None:
        self.reescalar = reescalar_imagenes(animacion, tamaño[0], tamaño[1])
        self.animaciones = animacion
        self.rectangulo_elemento = self.animaciones[0].get_rect()
        self.rectangulo_elemento.x = posiciones[0]
        self.rectangulo_elemento.y = posiciones[1]
        self.lados = obtener_rectangulo(self.rectangulo_elemento)

    def update(self, pantalla):
        pantalla.blit(self.animaciones[0], self.rectangulo_elemento)
