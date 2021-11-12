#Integrantes: Vocente Delgado, Thomas Pinda, Guillermo Ojeda, Camilo Lovera
import pygame
from pygame.locals import *
from Personaje import Personaje
from Proyectil import proyectil
pygame.init()
ventana_x = 800
ventana_y = 600
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("DEMO")
reloj = pygame.time.Clock()


def repintar_cuadro_juego():
    ventana.blit(imagen_fondo,(0,0))
    hero.dibujar(ventana)
    villano.dibujar(ventana)
    for bala in balas:
       bala.dibujarr(ventana)
    pygame.display.update()



repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
while repetir:

    imagen_fondo = pygame.image.load('pictures/fondo/ja.png')
    ruta_musica = "music/n.mp3"
    musica_fondo = pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(-1)   #desactivar activar

    hero=Personaje(600,400,"hero",int(ventana_y/2))#Agregar límite
    villano=Personaje(80,80,"malo",ventana_x)

    tanda_disparos = 0
    balas = []
    sonido_bala = pygame.mixer.Sound("music/hiyo.mp3")
    #sonido_golpe = pygame.mixer.Sound()
    esta_jugando=True
    while esta_jugando:
        reloj.tick(27)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
        teclas=pygame.key.get_pressed()
        hero.se_mueve_segun(teclas,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        villano.se_mueve_solo()
        if hero.se_encuentra_con(villano):
            hero.es_golpeado()
        if tanda_disparos > 0:
            tanda_disparos += 1
        if tanda_disparos > 20:
            tanda_disparos = 0

        for bala in balas:
            if villano.se_encuentra_con(bala):
                bala.impacta_a(villano)
                balas.pop(balas.index(bala))

            if bala.y < ventana_y and bala.y > 0:
                bala.y += bala.velocidad
            else:
                balas.pop(balas.index(bala))

        if teclas[pygame.K_x] and tanda_disparos == 0:
            if hero.va_izquierda:
                direccion = -1
            elif hero.va_derecha:
                direccion = -1
            else:
                direccion = -1
            if len(balas) < 5:
                balas.append(proyectil(round(hero.x + hero.ancho // 2), round(hero.y + hero.alto // 2), 10, (0,0,0), direccion))
                sonido_bala.play()
            tanda_disparos = 1
        repintar_cuadro_juego()
pygame.quit()
