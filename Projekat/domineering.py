import pygame
import sys
class Domineering:
    def __init__(self, stanje = [[]], x_na_potezu = True,screen=None,velicinaPolja=50,m=8,n=8,VI=False,dubina=4,x_max=True): #konstruktor
        self.stanje = stanje
        self.x_na_potezu = x_na_potezu
        self.screen=screen
        self.velicinaPolja=velicinaPolja
        self.m=m #m-broj vrsta
        self.n=n #n-broj kolona
        self.VI=VI
        self.dubina=dubina
        self.x_max=x_max
    def postavi_ekran(self,screen):
        self.screen=screen
    def pocetni_parametri(self):
        nema_pod_vrednost=True
        while nema_pod_vrednost:
                pom = input("Podrazumevane vrednosti?(D/N)\n")
                if pom == "D":
                    podrazumevane_vrednost = True
                    nema_pod_vrednost=False
                elif pom == "N":
                    podrazumevane_vrednost = False
                    nema_pod_vrednost=False
                elif pom == "d":
                    podrazumevane_vrednost = True
                    nema_pod_vrednost=False
                elif pom == "n":
                    podrazumevane_vrednost = False
                    nema_pod_vrednost=False
                    
        if not podrazumevane_vrednost:
            print("Unesite velicinu table u mxn")
            self.m=int(input())
            self.n=int(input())
            print("Unesite dubinu pretrage")
            self.dubina=int(input())
            nema_prvi_igrac = True
            nema_prvi_simbol = True            
            while nema_prvi_igrac:
                covek_prvi = input("Čovek igra prvi?(D/N)\n")
                if covek_prvi == "D":
                    nema_prvi_igrac = False
                    covek_prvi = True
                elif covek_prvi == "N":
                    nema_prvi_igrac = False
                    covek_prvi = False
                elif covek_prvi == "d":
                    nema_prvi_igrac = False
                    covek_prvi = True
                elif covek_prvi == "n":
                    nema_prvi_igrac = False
                    covek_prvi = False

            while nema_prvi_simbol:
                x_prvi = input("X igra prvi?(D/N)\n")
                if x_prvi == "D":
                    nema_prvi_simbol = False
                    x_prvi = True 
                elif x_prvi == "N":
                    nema_prvi_simbol = False
                    x_prvi = False 
                elif x_prvi == "d":
                    nema_prvi_simbol = False
                    x_prvi = True   
                elif x_prvi == "n":
                    nema_prvi_simbol = False
                    x_prvi = False 

            self.VI=not covek_prvi
            self.x_na_potezu=x_prvi


    def crtaj_tablu(self): #crtanje prazne tabele, sa brojevima i slovima polja
        self.velicinaPolja=int(self.screen.get_size()[0]/(self.n+2 if(self.n>self.m) else self.m+2))
        #boardscore=
        tabla=pygame.Surface(((self.n+1)*self.velicinaPolja,(self.m+1)*self.velicinaPolja))
        tabla.fill((0,0,0))
        p=True
        background=pygame.Surface(self.screen.get_size())
        background=background.convert()
        backgroundColor=(171,219,227)
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
        font_naslov=pygame.font.SysFont(None, int(self.screen.get_size()[0]/10))
        font=pygame.font.SysFont(None, int(self.velicinaPolja))

        if self.kraj_igre():
            igrac='O' if self.x_na_potezu else 'X'
            img = font_naslov.render(f'Pobednik je igrac {igrac}', True, (0,0,0))
        else:
            igrac='X' if self.x_na_potezu else 'O'
            img = font_naslov.render(f'Na potezu je igrac {igrac}', True, (0,0,0))

        rect = img.get_rect()
        pygame.draw.rect(img, (0,0,0), rect,-1)
        self.screen.blit(img,(int(self.velicinaPolja),int(self.velicinaPolja/4)))

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
    def pocetno_stanje(self): #postavlja matricu stanja na None
        self.stanje.clear()
        self.stanje = [[None for i in range(self.n)] for j in range(self.m)]

    def prikaz_stanja(self): #prikazuje trenutno stanje table
        for i in range(self.m-1,-1,-1):
            for j in range(self.n):
                if self.stanje[i][j]==0:
                    pygame.draw.rect(self.screen,(21,76,121),((j+1)*self.velicinaPolja,i*self.velicinaPolja+self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
                elif self.stanje[i][j]==1:
                    pygame.draw.rect(self.screen,(191, 32, 36),((j+1)*self.velicinaPolja,i*self.velicinaPolja+self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
    def proveri_klik(self,pos): #proverava da li je korisnik kliknuo na validnu poziciju na tabli
        (x,y)=pos
        x=x-self.velicinaPolja
        y=y-self.velicinaPolja
        if 0<x<self.velicinaPolja*(self.n) and 0<y<self.velicinaPolja*(self.m):
            return self.unesi_potez((int(y/self.velicinaPolja),int(x/self.velicinaPolja)))

    def unesi_potez(self,pos): #unos poteza kao i provera njegove validnosti
        if (self.potez_validan(pos)):
            if (self.x_na_potezu):
                self.stanje[pos[0]][pos[1]]=1
                self.stanje[pos[0]-1][pos[1]]=1
            elif (not self.x_na_potezu):
                self.stanje[pos[0]][pos[1]]=0
                self.stanje[pos[0]][pos[1]+1]=0
            self.x_na_potezu=not self.x_na_potezu
            return True
        else:
            print('Uneli ste nevalidan potez')
            return False

    def kraj_igre(self): #provera da li je igra došla do kraja
        for i in range(self.m):
            for j in range(self.n):
                if self.potez_validan((i,j)):
                    return False
        return True
    def potez_validan(self, pos): #provera validnosti poteza
        if self.x_na_potezu:
            if  not (len(self.stanje) > pos[0] >= 1):
                return False
            if not (len((self.stanje)[0]) > pos[1] >= 0):
                return False
            if not self.stanje[pos[0]][pos[1]] == None:
                return False
            if not self.stanje[pos[0]-1][pos[1]] == None:
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

    
def kraj_igre_za_stanje(stanje,x_igra): #provera da li je igra došla do kraja za odredjeno stanje
        for i in range(len(stanje)):
            for j in range(len(stanje[i])):
                if potez_validan_za_stanje(stanje,x_igra,(i,j)):
                    return False
        return True

def min_value(stanje,x_igra,x_max,dubina,alfa,beta,potez=None):
    if kraj_igre_za_stanje(stanje,x_igra):
        return (potez,-sys.maxsize) if x_igra==x_max else (potez,sys.maxsize) 
    lista_poteza=moguci_potezi(stanje,x_igra)
    if dubina==0 or lista_poteza is None or len(lista_poteza)==0:
        return (potez,odredi_heuristiku3(stanje,x_max))
    for s in lista_poteza:
        beta=min(beta,max_value(promena_stanja(stanje,x_igra,s),not x_igra,x_max,dubina-1,alfa,beta,s if potez is None else potez),key=lambda x:x[1])
        if beta[1]<=alfa[1]:
            break
    return beta

def max_value(stanje,x_igra,x_max,dubina,alfa,beta,potez=None):
    if kraj_igre_za_stanje(stanje,x_igra):
        return (potez,-sys.maxsize) if x_igra==x_max else (potez,sys.maxsize) 
    lista_poteza=moguci_potezi(stanje,x_igra)
    if dubina==0 or lista_poteza is None or len(lista_poteza)==0:
        return (potez,odredi_heuristiku3(stanje,x_max))
    for s in lista_poteza:
        alfa=max(alfa,min_value(promena_stanja(stanje,x_igra,s),not x_igra,x_max,dubina-1,alfa,beta,s if potez is None else potez),key=lambda x:x[1])
        if beta[1]<=alfa[1]:
            break
    return alfa

def minimax_alfa_beta(stanje,x_igra,x_max,dubina,alfa=(None,float('-inf')),beta=(None,float('inf'))):
    return max_value(stanje,x_igra,x_max,dubina,alfa,beta) if x_igra==x_max else min_value(stanje,x_igra,x_max,dubina,alfa,beta)


def potez_validan_za_stanje(zadato_stanje,x_igra,pos): #provera validnosti poteza za odredjeno stanje
        if x_igra:
            if  not (len(zadato_stanje) > pos[0] >= 1):
                return False
            if not (len((zadato_stanje)[0]) > pos[1] >= 0):
                return False
            if not zadato_stanje[pos[0]][pos[1]] == None:
                return False
            if not zadato_stanje[pos[0]-1][pos[1]] == None:
                return False
        else:
            if  not (len(zadato_stanje) > pos[0] >= 0):
                return False
            if not (len((zadato_stanje)[0]) - 1 > pos[1] >= 0):
                return False
            if not zadato_stanje[pos[0]][pos[1]] == None:
                return False
            if not zadato_stanje[pos[0]][pos[1]+1] == None:
                return False
        return True

def promena_stanja(ulazno_stanje,x_igra,pos):
    zadato_stanje= [[x for x in vrste] for vrste in ulazno_stanje]
    if potez_validan_za_stanje(zadato_stanje,x_igra,pos):
        if (x_igra):
                zadato_stanje[pos[0]][pos[1]]=1
                zadato_stanje[pos[0]-1][pos[1]]=1
        elif (not x_igra):
                zadato_stanje[pos[0]][pos[1]]=0
                zadato_stanje[pos[0]][pos[1]+1]=0
    return zadato_stanje

def moguci_potezi(zadato_stanje,x_igra):
    moguci_potezi = list()
    for i in range(len(zadato_stanje)):
        for j in range(len(zadato_stanje[i])):
            if potez_validan_za_stanje(zadato_stanje,x_igra,(i,j)):
                moguci_potezi.append((i,j))
    return moguci_potezi

def odredi_heuristiku(stanje):
    popunjene_kolone=0
    popunjene_vrste=0
    polu_popunjene_vrste=0
    polu_popunjene_kolone=0

    for vrsta in stanje:
        if all(map(lambda x: True if (x==0 or x==1) else False,vrsta)):
            popunjene_vrste+=1
        if vrsta.count(None)==1:
            polu_popunjene_vrste+=1
            
    for kolona in range(len(stanje[0])):
        if all(map(lambda x: True if (x==0 or x==1) else False,[stanje[vrsta][kolona] for vrsta in range(len(stanje))])):
            popunjene_kolone+=1  
        if [stanje[vrsta][kolona] for vrsta in range(len(stanje))].count(None)==1:
            polu_popunjene_kolone+=1

    return polu_popunjene_kolone+polu_popunjene_vrste+popunjene_kolone+popunjene_vrste

def odredi_heuristiku2(stanje,x_max):
    x_linija=0
    o_linija=0
    prazna_mesta=0
    for vrsta in range(len(stanje)):
        for kolona in range(len(stanje[vrsta])):
            if kolona<len(stanje[vrsta])-1: 
                if stanje[vrsta][kolona]==1 and stanje[vrsta][kolona+1]==1:
                    x_linija+=1
                elif stanje[vrsta][kolona]==0 and stanje[vrsta][kolona+1]==0:
                    o_linija+=1
            if vrsta<len(stanje)-1:
                if stanje[vrsta][kolona]==1 and stanje[vrsta+1][kolona]==1:
                    x_linija+=1
                elif vrsta < len(stanje)-1 and stanje[vrsta][kolona]==0 and stanje[vrsta+1][kolona]==0:
                    o_linija+=1
            if(stanje[vrsta][kolona] is None):
                prazna_mesta+=1
    
    return (x_linija-o_linija)*prazna_mesta if x_max==True else (o_linija-x_linija)*prazna_mesta

def odredi_heuristiku3(stanje,x_max):
    x_potezi=0
    o_potezi=0
    for vrsta in range(len(stanje)):
        for kolona in range(len(stanje[vrsta])):
            if potez_validan_za_stanje(stanje,True,(vrsta,kolona)):#x_igra
                x_potezi+=1
            if potez_validan_za_stanje(stanje,False,(vrsta,kolona)):#0_igra
                o_potezi+=1
    
    return (x_potezi-o_potezi) if x_max==True else (o_potezi-x_potezi)
