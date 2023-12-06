import pygame, sys
from pygame.locals import*
from Modulo import *
from CC_Vida import Vidas_personaje
from CC_Pantalla import*
from ZZZ_colores import*
from CC_textos import crear_texto

class Nivel:
    def __init__(self, pantalla, fondo, personaje, plataformas, plataformas_gravedad, enemigos, objetos, vidas,
                trampas, llave, puerta, movimientos_plataformas, movimientos: bool, jefe_nivel: bool, Jefe,
                color_rectangulo="white") -> None:
        self._slave = pantalla
        self.fondo = fondo
        
        self.jugador = personaje
        self.con_movimientos = movimientos
        self.enemigos = enemigos
        
        self.jefe = Jefe
        self.nivel_jefe = jefe_nivel
        
        self.plataformas = plataformas
        self.gravedad = plataformas_gravedad
        self.movimientos = movimientos_plataformas
        
        self.elementos = objetos
        self.trampas = trampas
        self.llave = llave
        self.final = puerta
        self.vidas = vidas
        
        self.empezo = False
        self.pausa = False
        self.color_rect = color_rectangulo
        
        self.tiempo_limite = 1 * 60000
        self.tiempo_inicial = pygame.time.get_ticks()


    def Teclas(self):
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.jugador.que_hace = "derecha"
        elif keys[K_a]:
            self.jugador.que_hace = "izquierda"
        elif keys[K_w]:
            self.jugador.que_hace = "salta"
        elif keys[K_e]:
            self.jugador.que_hace = "Ataque_Frutilla"
        elif keys[K_x]:
            self.jugador.que_hace = "ataque_patada"
        else:
            self.jugador.que_hace = "quieto"


    def dibujar_rect(self):
        if get_mode():
            # Rectángulos del jugador
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Red", self.jugador.lados[lado], 2)
            
            # Rectángulos de los proyectiles del jugador
            for proyectil in self.jugador.lista_proyectil:
                pygame.draw.rect(self._slave, "Red", proyectil.rectangulo, 2)
            
            # Rectángulos de las trampas
            for trampa in self.trampas:
                pygame.draw.rect(self._slave, "Red", trampa.rectangulo, 2)
            
            # Rectángulos de los enemigos
            for enemigo in self.enemigos:
                pygame.draw.rect(self._slave, "Red", enemigo.lados["main"], 2)
            
            for plataforma in self.plataformas:
                pygame.draw.rect(self._slave, "Red", plataforma.lados["main"], 2)
            
            for elemento in self.elementos:
                pygame.draw.rect(self._slave, "Red", elemento.lados["main"], 2)
            
            if self.jefe:
                for jefe in self.jefe:
                    pygame.draw.rect(self._slave, "Red", jefe.lados["main"], 2)


    def actualizar_elementos(self):
        for plataforma in self.plataformas:
            plataforma.animar(self._slave)
        
        if self.con_movimientos == True:
            for plataforma in self.movimientos:
                plataforma.update_movimiento(self._slave)
        
        if self.nivel_jefe == True:
            for jefe in self.jefe:
                jefe.update(self._slave, self.jugador, self.gravedad, self.enemigos, self.jugador.lista_proyectil)
        
        for trampa in self.trampas:
            trampa.update(self._slave, self.jugador)
        self.final.update(self._slave, self.jugador)
        self.jugador.update(self._slave, self.gravedad, self.enemigos, self.elementos, self.vidas, self.trampas, self.llave)
        
        for enemigo in self.enemigos:
            enemigo.update(self._slave, self.gravedad, self.jugador.lista_proyectil, self.jugador, self.enemigos)
        
        for proyectil in self.jugador.lista_proyectil:
            proyectil.update(self._slave, self.jugador)
        
        for llave in self.llave:
            llave.update(self._slave)


    def pausar(self):
        self.pausa = True


    def contador_reloj(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = max(0, self.tiempo_limite - (tiempo_actual - self.tiempo_inicial))
        minutos = tiempo_transcurrido // 60000
        segundos = (tiempo_transcurrido // 1000) % 60
        crear_texto(self._slave, f"{minutos:02d}:{segundos:02d}", (680, 10), (205, 92, 92), 40)
        
        if tiempo_transcurrido <= 0:
            print("¡Tiempo agotado! Perdiste o realizas alguna acción aquí.")


    def update(self, lista_eventos):
        if self.pausa:
            return
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            if evento.type == pygame.MOUSEBUTTONDOWN:  # toco la pantalla
                print(evento.pos)
        
        self._slave.blit(self.fondo, (0, 0))  # Dibujar fondo primero
        pygame.draw.rect(self._slave, self.color_rect, (0, 0, W, 50)) 
        self.dibujar_rect()
        self.Teclas()    
        Vidas_personaje(self._slave, self.jugador)
        self.actualizar_elementos()
        self.contador_reloj()
