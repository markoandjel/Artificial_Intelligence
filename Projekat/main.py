import pygame
from pygame.locals import *
from domineering import promena_stanja
from domineering import moguca_nova_stanja
from domineering import *
from domineering import Domineering
pygame.init()
clock=pygame.time.Clock()
# Postavi ekran
screen = pygame.display.set_mode([800, 800])

dominacija = Domineering(screen=screen)

dominacija.pocetni_parametri()
dominacija.pocetno_stanje()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            dominacija.proveri_klik(event.pos)
            min_max_value=minimax_alfa_beta([[x]for vrsta in dominacija.stanje for x in vrsta],dominacija.x_na_potezu,True,3)
            print(min_max_value)
            #dominacija.unesi_potez(min_max_value[0])
                
    dominacija.crtaj_tablu()
    dominacija.prikaz_stanja()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()