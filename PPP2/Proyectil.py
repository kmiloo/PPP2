import pygame

class proyectil(object):
    def __init__(self,x,y,radio,color,direccion):
        self.x=x
        self.y=y
        self.radio=radio
        self.color=color
        self.direccion=direccion
        self.velocidad=15 * direccion
        self.zona_impacto = (self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)

    def dibujarr(self, cuadro):
            
        self.zona_impacto = (self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)
        pygame.draw.circle(cuadro, self.color, (self.x,self.y),self.radio)

            
        
    def impacta_a(self,alguien):
        if alguien.salud > 0:
            alguien.salud -= 1
        else:
            del(alguien)