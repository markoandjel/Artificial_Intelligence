import pygame
from pygame.locals import *
from domineering import *
from domineering import Domineering
from timeit import default_timer as timer
pygame.init()
clock=pygame.time.Clock()
# Postavi ekran
screen = pygame.display.set_mode([800, 800])

dominacija = Domineering(screen=screen) #podesi x_max=False ako ti treba da Oks bude max igrac

dominacija.pocetni_parametri()
dominacija.pocetno_stanje()

running = True
dominacija.crtaj_tablu()
dominacija.prikaz_stanja()
pygame.display.flip()
if dominacija.VI:
    start=timer()
    min_max_value=minimax_alfa_beta([ [x for x in vrsta] for vrsta in dominacija.stanje],dominacija.x_na_potezu,dominacija.x_max,dominacija.dubina)
    end=timer()
    print(end-start)
    if not min_max_value[0]==None: 
        dominacija.unesi_potez(min_max_value[0])
        dominacija.crtaj_tablu()
        dominacija.prikaz_stanja()
        pygame.display.flip()

while running:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dominacija.proveri_klik(event.pos):
                dominacija.crtaj_tablu()
                dominacija.prikaz_stanja()
                pygame.display.flip()
                start=timer()
                min_max_value=minimax_alfa_beta([ [x for x in vrsta] for vrsta in dominacija.stanje],dominacija.x_na_potezu,dominacija.x_max,dominacija.dubina)
                end=timer()
                print(end-start)
                if not min_max_value[0]==None: 
                    dominacija.unesi_potez(min_max_value[0])
                    dominacija.crtaj_tablu()
                    dominacija.prikaz_stanja()
                    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()