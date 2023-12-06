from GUI_textbox import TextBox
from GUI_form import Form
from GUI_button_image import Button_Image
from GUI_label import Label
from ZZZ_colores import*
from ZZ_niveles import FormNiveles
from ZZ_sql import gestionar_base_datos


class FormDatos(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.titulo = Label(self._slave, 130, 17, 250, 80, "", "Verdana", 0, Salmon, "assets/img/pantalla/player.png")
        self.usuario = Label(self._slave, 20, 150, 150, 40, "Ingrese el usuario", "Verdana", 15, "White", "assets/img/pantalla/nada.png")
        
        self.nombre_jugador = TextBox(self._slave, x, y, 180, 150, 150, 30, naranja_claro, (235,182,250), "White", "White", 2, font = "Comic Sans", font_size=15, font_color= "White" )
        self.niveles = Button_Image(self._slave, x, y, 280, 320, 170, 70, "assets/img/pantalla/aceptar.png", self.btn_play, "Niveles")
        self._btn_home = Button_Image(screen=self._slave, x=100, y=320, master_x=x, master_y=y, w=170, h=70, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="assets/img/botones/menu.png")
        
        self.lista_widgets.append(self.titulo)
        self.lista_widgets.append(self.usuario)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.nombre_jugador)
        self.lista_widgets.append(self.niveles)
        self.render()

    def btn_play(self, texto):
        nombre_jugador = self.nombre_jugador.get_text()
        if nombre_jugador:
            gestionar_base_datos(nombre_jugador, 0)  # Guardar el nombre del jugador en la base de datos con un puntaje inicial de 0
            niveles = FormNiveles(self._master, 493, 229, 500, 550, (220,0,220), True, "assets/img/pantalla/nada.png")
            self.show_dialog(niveles)
            print(f"{nombre_jugador}")


    def btn_home_click(self, param): #Volver a los ajustes 
        self.end_dialog() 


    def render(self):
        self._slave.fill(self._color_background)


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                self.render()
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)