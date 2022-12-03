import pygame
class Domineering:
    def __init__(self, stanje = [[]], x_na_potezu = True,screen=None,velicinaPolja=50,m=8,n=8):
        self.stanje = stanje
        self.x_na_potezu = x_na_potezu
        self.screen=screen
        self.velicinaPolja=velicinaPolja
        self.m=m #m-broj vrsta
        self.n=n #n-broj kolona

    def crtaj_tablu(self):
        self.velicinaPolja=int(self.screen.get_size()[0]/(self.n+2 if(self.n>self.m) else self.m+2))
        tabla=pygame.Surface(((self.n+1)*self.velicinaPolja,(self.m+1)*self.velicinaPolja))
        tabla.fill((0,0,0))
        p=True
        background=pygame.Surface(self.screen.get_size())
        background=background.convert()
        backgroundColor=(255,240,125)
        background.fill(backgroundColor)
        self.screen.blit(background,(0,0))
        for i in range(self.m-1,-1,-1):
            for j in range(self.n):
                if(p):
                    pygame.draw.rect(tabla,(255,255,255),((j+1)*self.velicinaPolja,i*self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
                p=not p
            if self.n%2==0:
                p=not p
        pygame.draw.rect(tabla,backgroundColor,(0,0,self.velicinaPolja,self.velicinaPolja*self.m))
        pygame.draw.rect(tabla,backgroundColor,(0,self.velicinaPolja*self.m,self.velicinaPolja*(self.n+1),self.velicinaPolja))
        font=pygame.font.SysFont(None, int(self.velicinaPolja))
        pomeraj=self.velicinaPolja/4
        
        for i in range (self.n): #crtanje slova
            img = font.render(chr(ord('a')+i), True, (0,0,0))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,0), rect,-1)
            tabla.blit(img,(self.velicinaPolja*(i+1)+pomeraj,self.m*self.velicinaPolja))

        for i in range (self.m,0,-1): #crtanje brojeva
            img = font.render(f"{self.m-i+1}", True, (0,0,0))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,0), rect,-1)
            tabla.blit(img,(pomeraj*2,self.velicinaPolja*(i-1)+pomeraj))
        
        self.screen.blit(tabla,(0,self.velicinaPolja))
    def pocetno_stanje(self):
        self.stanje.clear()
        self.stanje = [[None for i in range(self.n)] for j in range(self.m)]

    def prikaz_stanja(self):
        for i in range(self.m-1,-1,-1):
            for j in range(self.n):
                if self.stanje[i][j]==0:
                    pygame.draw.rect(self.screen,(47, 44, 255),((j+1)*self.velicinaPolja,i*self.velicinaPolja+self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
                elif self.stanje[i][j]==1:
                    pygame.draw.rect(self.screen,(222, 56, 44),((j+1)*self.velicinaPolja,i*self.velicinaPolja+self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
    def proveri_klik(self,pos):
        (x,y)=pos
        x=x-self.velicinaPolja
        y=y-self.velicinaPolja
        if 0<x<self.velicinaPolja*(self.n) and 0<y<self.velicinaPolja*(self.m):
            self.unesi_potez((int(y/self.velicinaPolja),int(x/self.velicinaPolja)))

    def unesi_potez(self,pos):
        if (self.potez_validan(pos)):
            if (self.x_na_potezu):
                self.stanje[pos[0]][pos[1]]=1
                self.stanje[pos[0]+1][pos[1]]=1
            elif (not self.x_na_potezu):
                self.stanje[pos[0]][pos[1]]=0
                self.stanje[pos[0]][pos[1]+1]=0
            self.x_na_potezu=not self.x_na_potezu
        else:
            print('Uneli ste nevalidan potez')

    def kraj_igre(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.potez_validan((i,j)):
                    return False
        return True
    def potez_validan(self, pos):
        if self.x_na_potezu:
            if  not (len(self.stanje) - 1 > pos[0] >= 0):
                return False
            if not (len((self.stanje)[0]) > pos[1] >= 0):
                return False
            if not self.stanje[pos[0]][pos[1]] == None:
                return False
            if not self.stanje[pos[0]+1][pos[1]] == None:
                return False
        else:
            if  not (len(self.stanje) > pos[0] >= 0):
                return False
            if not (len((self.stanje)[0]) - 1 > pos[1] >= 0):
                return False
            if not self.stanje[pos[0]][pos[1]] == None:
                return False
            if not self.stanje[pos[0]][pos[1]+1] == None:
                return False
        return True