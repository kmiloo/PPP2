import pygame

pygame.init()
ventana_x = 800
ventana_y = 600
ventana = pygame.display.set_mode((ventana_x,ventana_y))
class Personaje(object):

    def __init__(self, x, y, fuente, limite):
        self.x = x
        self.y = y
        self.velocidad = 10
        self.va_izquierda = False
        self.va_derecha = False
        self.va_arriba = False
        self.va_abajo = False
        self.contador_pasos = 0
        fuente += "/"
        self.quieto = pygame.image.load("pictures/"+fuente+"a.png")
        self.ancho = self.quieto.get_width()
        self.alto = self.quieto.get_height()
        self.camino = (self.x, limite)
        self.salud = 10
        self.zona_impacto = (self.x + 10, self.y + 15, 55, 50)

    def dibujar(self, cuadro):
        cuadro.blit(self.quieto, (self.x,self.y))
        pygame.draw.rect(cuadro, (255,0,0), (self.x+5, self.y -20, 50, 10))
        pygame.draw.rect(cuadro, (0,128,0), (self.x+5, self.y -20, 50 - (5 * (10 - self.salud)), 10))
        self.zona_impacto = (self.x + 10 , self.y + 15, 55, 50)
        #pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto,2)

    def se_mueve_segun(self, k, iz, de, ar, ab):
            if k[iz] and self.x > self.velocidad:
                self.x -= self.velocidad
                self.va_izquierda = True
                self.va_derecha = False

            if k[de] and self.x < ventana_x - self.ancho - self.velocidad:
                self.x += self.velocidad
                self.va_derecha = True
                self.va_izquierda = False

            if k[ar] and self.y > self.velocidad:
                self.y -= self.velocidad


            if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
                self.y += self.velocidad

                
    def se_mueve_solo(self):
        if self.velocidad > 0:
            if self.x + self.velocidad < self.camino[1]:
                self.x += self.velocidad 
                self.va_derecha = True
                self.va_izquierda = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0
        else:
            if self.x - self.velocidad > self.camino[0]:
                self.x += self.velocidad 
                self.va_izquierda = True
                self.va_derecha = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0

    def se_encuentra_con(self, alguien):
        R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
        R1_ar = self.zona_impacto[1]
        R1_iz = self.zona_impacto[0]
        R1_de = self.zona_impacto[0] + self.zona_impacto[2]
        R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
        R2_ar = alguien.zona_impacto[1]
        R2_iz = alguien.zona_impacto[0]
        R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]

        return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar

    def es_golpeado(self):
        self.x = 100
        self.y = 410
        self.salud -= 5
        pygame.time.delay(500)
