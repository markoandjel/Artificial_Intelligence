import pygame
from pygame.locals import *
from domineering import promena_stanja
from domineering import moguca_nova_stanja
from domineering import Domineering
pygame.init()
clock=pygame.time.Clock()
# Postavi ekran
screen = pygame.display.set_mode([800, 800])


dominacija = Domineering(screen=screen)

dominacija.pocetni_parametri()

dominacija.pocetno_stanje()


nova_stanja=moguca_nova_stanja([[None,None,None],[None,None,None],[None,None,None]],False)
print(nova_stanja)
running = True

p=promena_stanja([[None,None,None],[None,None,None],[None,None,None]],False,(2,2))
print(p)
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