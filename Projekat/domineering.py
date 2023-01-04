import pygame
class Domineering:
    def __init__(self, stanje = [[]], x_na_potezu = True,screen=None,velicinaPolja=50,m=8,n=8,VI=False): #konstruktor
        self.stanje = stanje
        self.x_na_potezu = x_na_potezu
        self.screen=screen
        self.velicinaPolja=velicinaPolja
        self.m=m #m-broj vrsta
        self.n=n #n-broj kolona
        self.VI=VI
    
    def pocetni_parametri(self):
        print("Unesite velicinu table u mxn")
        self.m=int(input())
        self.n=int(input())
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
        font=pygame.font.SysFont(None, int(self.velicinaPolja))

        if self.kraj_igre():
            igrac='O' if self.x_na_potezu else 'X'
            img = font.render(f'Pobednik je igrac {igrac}', True, (0,0,0))
        else:
            igrac='X' if self.x_na_potezu else 'O'
            img = font.render(f'Na potezu je igrac {igrac}', True, (0,0,0))

        
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
                    pygame.draw.rect(self.screen,(47, 44, 255),((j+1)*self.velicinaPolja,i*self.velicinaPolja+self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
                elif self.stanje[i][j]==1:
                    pygame.draw.rect(self.screen,(222, 56, 44),((j+1)*self.velicinaPolja,i*self.velicinaPolja+self.velicinaPolja,self.velicinaPolja,self.velicinaPolja))
    def proveri_klik(self,pos): #proverava da li je korisnik kliknuo na validnu poziciju na tabli
        (x,y)=pos
        x=x-self.velicinaPolja
        y=y-self.velicinaPolja
        if 0<x<self.velicinaPolja*(self.n) and 0<y<self.velicinaPolja*(self.m):
            self.unesi_potez((int(y/self.velicinaPolja),int(x/self.velicinaPolja)))

    def unesi_potez(self,pos): #unos poteza kao i provera njegove validnosti
        if (self.potez_validan(pos)):
            if (self.x_na_potezu):
                self.stanje[pos[0]][pos[1]]=1
                self.stanje[pos[0]-1][pos[1]]=1
            elif (not self.x_na_potezu):
                self.stanje[pos[0]][pos[1]]=0
                self.stanje[pos[0]][pos[1]+1]=0
            self.x_na_potezu=not self.x_na_potezu
        else:
            print('Uneli ste nevalidan potez')

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

def promena_stanja(zadato_stanje,x_igra,pos):
    if potez_validan_za_stanje(zadato_stanje,x_igra,pos):
        if (x_igra):
                zadato_stanje[pos[0]][pos[1]]=1
                zadato_stanje[pos[0]-1][pos[1]]=1
        elif (not x_igra):
                zadato_stanje[pos[0]][pos[1]]=0
                zadato_stanje[pos[0]][pos[1]+1]=0
    return zadato_stanje

def moguca_nova_stanja(zadato_stanje,x_igra):
    nova_stanja = list()
    for i in range(len(zadato_stanje)):
        for j in range(len(zadato_stanje[i])):
            privremeno_stanje = [vrste.copy() for vrste in zadato_stanje]
            if potez_validan_za_stanje(zadato_stanje,x_igra,(i,j)):
                nova_stanja.append(promena_stanja(privremeno_stanje,x_igra,(i,j)))
    return nova_stanja

#def odredi_heuristiku_za_stanje(stanje):

def min_stanje(lista_stanja):
    return min(lista_stanja)

def odredi_heurustiku(stanje):
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
        if all(map(lambda x: True if (x==0 or x==1) else False,[stanje[vrsta,kolona] for vrsta in range(len(stanje))])):
            popunjene_kolone+=1  
        if [stanje[vrsta,kolona] for vrsta in range(len(stanje))].count(None)==1:
            polu_popunjene_kolone+=1

    return polu_popunjene_kolone+polu_popunjene_vrste+popunjene_kolone+popunjene_vrste

    
    

def heuristic(state):
    # Count the number of rows and columns that are completely filled with dominos
    filled_rows = sum(state.row_filled(i) for i in range(state.rows))
    filled_cols = sum(state.col_filled(i) for i in range(state.cols))

    # Count the number of rows and columns that have only one empty space
    half_filled_rows = sum(state.row_filled(i) == state.cols - 1 for i in range(state.rows))
    half_filled_cols = sum(state.col_filled(i) == state.rows - 1 for i in range(state.cols))

    # Calculate the value of the current state
    value = filled_rows + filled_cols + half_filled_rows + half_filled_cols

    # If the current player is the maximizing player, return the value
    # If the current player is the minimizing player, return -value
    return value if state.current_player == MAXIMIZING_PLAYER else -value

