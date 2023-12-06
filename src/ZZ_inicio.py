import pygame, sys
from GUI_form import Form
from GUI_button_image import Button_Image
from ZZ_ajustes import FormAjustes
from ZZ_datos import FormDatos
from ZZZ_colores import*


class Inicio(Form):
    def __init__(self, screen, x, y, w, h,  active, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.btn_ajustes = Button_Image(self._slave, x, y, 180, 100, 200, 70, "assets/img/botones/boton_ajustes.png", self.btn_ajustes, "Ajustes")
        self.btn_niveles = Button_Image(self._slave, x, y, 180, 30, 200, 70, "assets/img/botones/bptpn_partida.png", self.btn_play, "Niveles")
        self.btn_salir = Button_Image(self._slave, x, y, 185, 170, 200, 70, "assets/img/botones/boton_salir.png", self.btn_salir, "salir")
        # self.btn_ranking = Button_Image(self._slave, x, y, 180, 170, 200, 70, "assets/img/botones/boton_ranking.png", self.btn_ranking, "ranking")

        self.lista_widgets.append(self.btn_niveles)
        self.lista_widgets.append(self.btn_ajustes)#rankin otra ventana
        # self.lista_widgets.append(self.btn_ranking)
        self.lista_widgets.append(self.btn_salir)

        
    def update(self, lista_eventos): # actualizar elementos en mi formulario
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)
            
    def btn_salir(self, texto):
        pygame.quit()
        sys.exit()
    
    def btn_ajustes(self, texto):
        opciones = FormAjustes(self._master, 493, 229, 500, 550, naranja_tirando_a_rojo, naranja_claro, 3, True)
        self.show_dialog(opciones)


    def btn_play(self, texto):
        usuario = FormDatos(self.pantalla , 493, 230, 500, 400, naranja_tirando_a_rojo, naranja_claro, 3, True)
        self.show_dialog(usuario)

    # def btn_ranking(self, texto):
    #     ranking = FormRanking(self._master, 493, 230, 500, 550, rojo_claro, rojo_oscuro, 3, True)
    #     self.show_dialog(ranking)