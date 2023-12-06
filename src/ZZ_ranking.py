# from GUI_button import *
# from GUI_slider import *
# from GUI_textbox import *
# from GUI_label import *
# from GUI_form import *
# from GUI_button_image import *
# from ZZZ_colores import*
# import sqlite3


# class FormRanking(Form):
#     def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
#         super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        

#         self.titulo = Label(self._slave, 115, 10, 250, 80, "", "Verdana", 0, Salmon, "sin_fondo\\fHello_KItty_Adventure__3_-removebg-preview.png")
#         self._btn_home = Button_Image(screen=self._slave, x=180, y=480, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__10_-removebg-preview.png")

#         self.lista_widgets.append(self.titulo)
#         self.lista_widgets.append(self._btn_home)

#         self.render()

#     def btn_home_click(self, param): #Volver a los ajustes 
#         self.end_dialog() 

#     def render(self):
#         self._slave.fill(self._color_background)

#     def obtener_datos_sql(self):
#         conexion = sqlite3.connect("Usuarios.db")
#         cursor = conexion.cursor()

#         cursor.execute("SELECT Nombre, score FROM usuario")
#         datos = cursor.fetchall()

#         conexion.close()

#         pos_inicial_x = 100
#         pos_inicial_y = 100
#         pos_puntos_x = 120
#         pos_puntos_y = 130

#         for dato in datos:
#             nombre = dato[0]
#             score = dato[1]

#             # Crea un objeto Label para mostrar el nombre y puntaje
#             label_jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, 250, 30, f"Nombre: {nombre}", "Verdana", 23, (255, 255, 255), "Imagenes\\nada.png")
#             label_puntos = Label(self._slave, pos_puntos_x, pos_puntos_y, 250, 30, f"Score: {score}", "Verdana", 23, (255, 255, 255), "Imagenes\\nada.png")
#             self.lista_widgets.append(label_jugador)
#             self.lista_widgets.append(label_puntos)

#             pos_inicial_y += 70
#             pos_puntos_y += 80
            

#         self.render()

#     def update(self, lista_eventos):
#         if self.active:
#             self.draw()
#             self.render()
#             self.obtener_datos_sql()
#             for wid in self.lista_widgets:
#                 wid.update(lista_eventos)
            

