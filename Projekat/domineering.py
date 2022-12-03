import pygame
class Domineering:
    def __init__(self, tabla = [[]], x_na_potezu = True,velicinaPolja=50,screen=None):
        self.tabla = tabla
        self.x_na_potezu = x_na_potezu
        self.velicinaPolja=velicinaPolja
        self.screen=screen

    def crtajTablu(self,m:int,n:int): #m-broj vrsta, n-broj kolona
        tabla=pygame.Surface(((n+1)*self.velicinaPolja,(m+1)*self.velicinaPolja))
        tabla.fill((0,0,0))
        p=True
        background=pygame.Surface(self.screen.get_size())
        background=background.convert()
        backgroundColor=(255,240,125)
        background.fill(backgroundColor)
        self.screen.blit(background,(0,0))
        for i in range(m-1,-1,-1):
            for j in range(n):
                if(p):
                    pygame.draw.rect(tabla,(255,255,255),((j+1)*self.velicinaPolja,i*self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
                p=not p
            if n%2==0:
                p=not p
        pygame.draw.rect(tabla,backgroundColor,(0,0,self.velicinaPolja,self.velicinaPolja*m))
        pygame.draw.rect(tabla,backgroundColor,(0,self.velicinaPolja*m,self.velicinaPolja*(n+1),self.velicinaPolja))
        font=pygame.font.SysFont(None, 44)
        pomeraj=15
        
        for i in range (n):
            img = font.render(chr(ord('a')+i), True, (0,0,0))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,0), rect,-1)
            tabla.blit(img,(self.velicinaPolja*(i+1)+pomeraj,m*self.velicinaPolja))

        for i in range (m,0,-1):
            img = font.render(f"{i}", True, (0,0,0))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,0), rect,-1)
            tabla.blit(img,(pomeraj,self.velicinaPolja*(i-1)+pomeraj))
        return tabla