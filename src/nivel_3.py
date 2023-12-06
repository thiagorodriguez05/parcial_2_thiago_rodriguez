import pygame
from AA_itadori import Personaje
from AA_archivo_itadori import tamaño, diccionario_animaciones, posicion_inicial
from DD_Plataformas import Plataformas
from AA_Enemigos import enemigo
from AA_archivos_enemigo import Tamaño_enemigo, diccionario_enemigo
from CC_Recolectar import Elementos
from CC_Archivos_objetos import animaciones_dedos, animacion_mas_vidas, animaciones_llave
from AA_puerta_final import Puerta, diccionario_puerta
from FF_Crear_nivel import Nivel
from DD_piso import Piso
from AA_trampas import Trampas
from CC_Pantalla import*
from AA_boss import lista_jefe
from ZZZ_colores import*

pygame.init()
pygame.font.init()


class nivelTres(Nivel):
    def __init__(self, pantalla: pygame.surface) -> None:
        fondo = pygame.image.load("assets/img/niveles/lvl_3.png")
        fondo = pygame.transform.scale(fondo, (W, H))

        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 8)
        piso = Piso(0, 800, W, 20)
        piso.crear_piso(pantalla)

        # contador_reloj(tiempo_inicial, self._slave)
        # Vidas_personaje(self._slave, self.jugador)

        plataforma_M_uno = Plataformas("assets\img\platafromas\plataforma_1.png", (467, 675), (400,75),(812, 682))
        plataforma_dos = Plataformas("assets\img\platafromas\plataforma_1.png", (788, 565), (500, 75), (1235, 509))### dejo 
        plataforma_tres = Plataformas("assets\img\platafromas\plataforma_1.png", (347, 361), (91, 60), (493, 419))# mover - (347, 361)
        plataforma_cuatro = Plataformas("assets\img\platafromas\plataforma_1.png",(0, 293), (300, 60), (201, 298))
        plataforma_cinco = Plataformas("assets\img\platafromas\plataforma_1.png",(446, 200), (610, 75), (974, 160))
        plataforma_seis = Plataformas("assets\img\platafromas\plataforma_1.png", (1105, 344), (550, 75), (1495, 275))#mas abajo -(1105, 344) mas largo - 550
        plataforma_siete = Plataformas("assets\img\platafromas\plataforma_1.png", (530, 467), (90, 75), (1495, 275)) #mas corto 90

        lista_movimientos = [plataforma_M_uno]
        lista_plataformas = [plataforma_dos, plataforma_tres, plataforma_cuatro,
                            plataforma_cinco, plataforma_seis, plataforma_siete]

        lista_gravedad = [piso.lados["main"],plataforma_M_uno.lados["top"], plataforma_dos.lados["top"],
                    plataforma_tres.lados["top"], plataforma_cuatro.lados["top"], 
                    plataforma_cinco.lados["top"], plataforma_seis.lados["top"], plataforma_siete.lados["top"]]
        
        enemigo_uno = enemigo( (788, 488),(1188, 493), diccionario_enemigo, Tamaño_enemigo, 2)# (788, 488) a (1188, 493)
        enemigo_dos = enemigo((462, 127), (932, 102), diccionario_enemigo, Tamaño_enemigo, 2)
        enemigo_tres = enemigo((1108, 257) ,(1385, 260), diccionario_enemigo, Tamaño_enemigo, 2)

        Enemigos = [enemigo_uno, enemigo_dos, enemigo_tres]

        dedos_uno = Elementos(animaciones_dedos, (519, 620), (50,50))#(519, 620)
        dedos_dos = Elementos(animaciones_dedos, (639, 620), (50,50))#(639, 620)
        dedos_tres = Elementos(animaciones_dedos, (795, 497), (50,50))#(795, 497)
        dedos_cuatro = Elementos(animaciones_dedos, (904, 497), (50,50))#(904, 497)
        dedos_cinco = Elementos(animaciones_dedos, (1024, 497), (50,50))#(1024, 497)
        dedos_seis = Elementos(animaciones_dedos, (1136, 502), (50,50))#(1136, 502)
        dedos_siete = Elementos(animaciones_dedos, (556, 425), (50,50))#(556, 425)
        dedos_ocho = Elementos(animaciones_dedos, (373, 311), (50,50))#(373, 311)
        dedos_nueve = Elementos(animaciones_dedos, (235, 245), (50,50))#(235, 245)
        dedos_diez = Elementos(animaciones_dedos, (137, 245), (50,50))#(137, 245)
        dedos_once = Elementos(animaciones_dedos, (857, 150), (50,50))#(857, 150)
        dedos_doce  =Elementos(animaciones_dedos, (771, 150), (50,50))#(771, 150)
        dedos_trece = Elementos(animaciones_dedos, (623, 150), (50,50))#(623, 150)
        dedos_catorce = Elementos(animaciones_dedos, (498, 150), (50,50))#(498, 150)
        dedos_quince = Elementos(animaciones_dedos, (1398, 295), (50,50))#(1398, 295)
        dedos_diezseis = Elementos(animaciones_dedos, (1275, 295), (50,50))#(1275, 295)
        dedos_diezsiete = Elementos(animaciones_dedos, (1275, 295), (50,50))#(1275, 295)

        lista_objetos = [dedos_uno, dedos_dos, dedos_tres, dedos_cuatro, dedos_cinco, 
                        dedos_seis, dedos_siete, dedos_ocho, dedos_nueve, dedos_diez, 
                        dedos_once, dedos_doce, dedos_trece, dedos_catorce, dedos_quince,
                        dedos_diezseis, dedos_diezsiete]
        
        elemento_recuperar_uno = Elementos(animacion_mas_vidas, (948, 151), (40,40))# (948, 151)
        lista_recuperar = [elemento_recuperar_uno]
        llave = Elementos(animaciones_llave, (45, 226), (60, 60))
        lista_llave_uno = [llave]
        flor_trampa = Trampas((331, 48), (331, 266), (80,80))# (331, 48) a (331, 266)
        listas_trampas = [flor_trampa]
        puerta_nivel_dos = Puerta(diccionario_puerta, (1357, 670))# - (1356, 617)

        super().__init__(pantalla, fondo, mi_personaje, lista_plataformas, lista_gravedad, 
                        Enemigos, lista_objetos, lista_recuperar, listas_trampas, lista_llave_uno, 
                        puerta_nivel_dos, lista_movimientos, True, True, lista_jefe, color_gris_claro)

