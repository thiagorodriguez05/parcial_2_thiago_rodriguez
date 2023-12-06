from nivel_1 import *
from nivel_2 import *
from nivel_3 import*

class ManejadorNiveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"Nivel_1": nivelUno, "Nivel_2": nivelDos,"Nivel_3": nivelTres}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)

