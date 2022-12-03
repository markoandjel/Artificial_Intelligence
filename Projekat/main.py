import pygame
from pygame.locals import *
from domineering import Domineering
pygame.init()
clock=pygame.time.Clock()
# Postavi ekran
screen = pygame.display.set_mode([800, 800])
dominacija = Domineering(screen=screen,m=7,n=7)

dominacija.pocetno_stanje()
dominacija.unesi_potez((2,2))
dominacija.unesi_potez((5,5))

dominacija.unesi_potez((1,5))

dominacija.unesi_potez((0,3))
running = True
  
while running:
    #igrac='X' if dominacija.x_na_potezu else 'O'
    #print(f'Na potezu je igrac {igrac}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            dominacija.proveri_klik(event.pos)            
    dominacija.crtaj_tablu()
    dominacija.prikaz_stanja()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()