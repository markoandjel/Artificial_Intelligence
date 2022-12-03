import pygame
from pygame.locals import *
from domineering import Domineering
pygame.init()
clock=pygame.time.Clock()
# Postavi ekran
screen = pygame.display.set_mode([800, 800])


dominacija = Domineering(screen=screen)

dominacija.pocetni_parametri()

dominacija.pocetno_stanje()
#dominacija.unesi_potez((2,2))
#dominacija.unesi_potez((5,5))
#dominacija.unesi_potez((1,5))
#dominacija.unesi_potez((0,3))
running = True
  
while running:
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