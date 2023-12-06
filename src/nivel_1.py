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
from ZZZ_colores import*

pygame.init()
pygame.font.init()



class nivelUno(Nivel):
    def __init__(self, pantalla: pygame.surface) -> None:
        fondo = pygame.image.load("assets/img/niveles/lvl_1.png")
        fondo = pygame.transform.scale(fondo, (W, H))
        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10)
        
        piso = Piso(0, 800, W, 20)
        piso.crear_piso(pantalla)
        
        plataforma_uno = Plataformas("assets\img\platafromas\plataforma_1.png",(276, 633),(400,75), (500,620))
        plataforma_dos = Plataformas("assets\img\platafromas\plataforma_1.png",(606, 513), (400,75), (1076, 503))
        plataforma_tres = Plataformas("assets\img\platafromas\plataforma_1.png",(1024, 410), (400,75), (0, 0))
        plataforma_cuatro = Plataformas("assets\img\platafromas\plataforma_1.png",(520, 285), (400,75), (0, 0))
        plataforma_cinco = Plataformas("assets\img\platafromas\plataforma_1.png",(26, 180), (400,75), (509, 193))
        
        lista_plataformas_uno = [plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro, plataforma_cinco]
        
        lista_gravedad_uno = [piso.lados["top"], plataforma_uno.lados["top"], plataforma_dos.lados["top"],
                    plataforma_tres.lados["top"], plataforma_cuatro.lados["top"], plataforma_cinco.lados["top"]]
        
        enemigo_uno = enemigo((284, 545),(597, 557),diccionario_enemigo, Tamaño_enemigo, 1)
        enemigo_dos = enemigo((525, 202), (819, 200), diccionario_enemigo, Tamaño_enemigo, 1)
        enemigo_tres = enemigo((706, 657), (1265, 654), diccionario_enemigo, Tamaño_enemigo, 1)
        
        Enemigos = [enemigo_uno, enemigo_dos, enemigo_tres]
        
        moneda_uno = Elementos(animaciones_dedos, (309, 581), (50,50))
        moneda_dos = Elementos(animaciones_dedos, (414, 582), (50,50))
        moneda_tres = Elementos(animaciones_dedos, (542, 585), (50,50))
        moneda_cuatro = Elementos(animaciones_dedos, (652, 464), (50,50))
        moneda_cinco = Elementos(animaciones_dedos, (765, 462), (50,50))
        moneda_seis = Elementos(animaciones_dedos, (879, 463), (50,50))
        moneda_siete = Elementos(animaciones_dedos, (1071, 363), (50,50))
        moneda_ocho = Elementos(animaciones_dedos, (1190, 359), (50,50))
        moneda_nueve = Elementos(animaciones_dedos,(546, 243), (50,50))
        moneda_diez = Elementos(animaciones_dedos,(657, 244), (50,50))
        moneda_once = Elementos(animaciones_dedos,(838, 244), (50,50))
        
        lista_objetos = [moneda_uno, moneda_dos, moneda_tres, moneda_cuatro, moneda_cinco, 
                        moneda_seis, moneda_siete, moneda_ocho, moneda_nueve,moneda_diez,
                        moneda_once]
        
        elemento_recuperar_uno = Elementos(animacion_mas_vidas, (1328, 364), (40,40))
        lista_recuperar = [elemento_recuperar_uno]
        
        llave_nivel_uno = Elementos(animaciones_llave, (72, 107), (60, 60))
        lista_llave_uno = [llave_nivel_uno]
        
        flor_trampa_uno = Trampas((1292, 72), (1287, 364), (80,80))
        listas_trampas = [flor_trampa_uno]
        
        puerta_nivel_uno = Puerta(diccionario_puerta, (1353, 670))
        
        super().__init__(pantalla, fondo, mi_personaje, lista_plataformas_uno, lista_gravedad_uno, 
                        Enemigos, lista_objetos, lista_recuperar, listas_trampas, lista_llave_uno, 
                        puerta_nivel_uno, None, False,  False, None, color_celeste_claro)
