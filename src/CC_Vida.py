import pygame

def Vidas_personaje(pantalla, personaje):
    if personaje.vidas <= 0:
        imagen_path = "assets/img/vidas/vidas_6.png" 
    elif personaje.vidas == 1:
        imagen_path = "assets/img/vidas/vidas_5.png"  
    elif personaje.vidas == 2:
        imagen_path = "assets/img/vidas/vidas_3.png"  
    elif personaje.vidas == 3:
        imagen_path = "assets/img/vidas/vidas_1.png"  
    elif personaje.vidas == 4:
        imagen_path = "assets/img/vidas/vidas_1.png" 
    
    imagen = pygame.image.load(imagen_path)  
    imagen_redimensionada = pygame.transform.scale(imagen, (40, 40)) 
    
    imagen_rect = imagen_redimensionada.get_rect()  
    imagen_rect.x = 50 
    imagen_rect.y = 5  
    
    pantalla.blit(imagen_redimensionada, imagen_rect)


def vidas_jefe(pantalla, vidas):
    if vidas <= 0:
        imagen_path = "assets/img/vidas/vida_jefe_6.png" 
    elif vidas == 1:
        imagen_path = "assets/img/vidas/vida_jefe_5.png"  
    elif vidas == 2:
        imagen_path = "assets/img/vidas/vida_jefe_4.png"  
    elif vidas == 3:
        imagen_path = "assets/img/vidas/vida_jefe_3.png"  
    elif vidas == 4:
        imagen_path = "assets/img/vidas/vida_jefe_2.png" 
    elif vidas == 5:
        imagen_path = "assets/img/vidas/vida_jefe_1.png"
    
    imagen = pygame.image.load(imagen_path)  
    imagen_redimensionada = pygame.transform.scale(imagen, (180, 40)) 
    imagen_rect = imagen_redimensionada.get_rect()  
    imagen_rect.x = 890
    imagen_rect.y = 7 
    
    pantalla.blit(imagen_redimensionada, imagen_rect)