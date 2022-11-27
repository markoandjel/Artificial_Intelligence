import pygame
pygame.init()

# Postavi ekran
screen = pygame.display.set_mode([500, 500])
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,240,125))
p=False
m=8
n=8
velicinaPolja=50
figureX=pygame.Surface((velicinaPolja,2*velicinaPolja))
pygame.draw.rect(figureX,(255,80,80),(0,0,velicinaPolja,2*velicinaPolja))
tabla=pygame.Surface((n*velicinaPolja,m*velicinaPolja))
tabla.fill((0,0,0))
for i in range(m):
    for j in range(n,-1,-1):
        if(p):
            pygame.draw.rect(tabla,(255,255,255),(i*velicinaPolja,j*velicinaPolja,velicinaPolja,velicinaPolja))
        p=not p

# Radi dok ti ne kažem kraj 
running = True
while running:

    # Klik na izađi dugme? 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bela boja ispune
    screen.blit(background,(0,0))
    screen.blit(tabla,(50,50))

    screen.blit(figureX,(50,150))
    # Nacrtaj nešto 
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Prikazi to nešto
    pygame.display.flip()

# Dosta je! Gasi sliku!
pygame.quit()