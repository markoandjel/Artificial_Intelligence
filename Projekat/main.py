import pygame
from pygame.locals import *
from domineering import Domineering
pygame.init()

# Postavi ekran



screen = pygame.display.set_mode([800, 800])
dominacija = Domineering(screen=screen)


#figureX=pygame.Surface((velicinaPolja,2*velicinaPolja))
#pygame.draw.rect(figureX,(255,80,80),(0,0,velicinaPolja,2*velicinaPolja))


# Radi dok ti ne kažem kraj 
running = True
while running:

    # Klik na izađi dugme? 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(dominacija.crtajTablu(8,8),(50,50))
    

    #screen.blit(figureX,(50,150))
    # Nacrtaj nešto 
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Prikazi to nešto
    pygame.display.flip()

# Dosta je! Gasi sliku!
pygame.quit()