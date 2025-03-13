import pygame
  
pygame.init()
  
ganha = pygame.display.set_mode((500, 400))
  
pygame.display.set_caption("Selection sort")
  
x = 40
y = 40
  
largura = 20
  
barras = [20, 100, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]
  
run = True
  
def show(barras):
    for i in range(len(barras)):
        pygame.draw.rect(ganha, (255, 0, 0), (x + 30 * i, y, largura, barras[i]))
  
while run:
    execute = False
    pygame.time.delay(10)
    chave = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if chave[pygame.K_SPACE]:
        execute = True
    if execute == False:
        ganha.fill((0, 0, 0))
        show(barras)
        pygame.display.update()
    else:
        size = len(barras)
        for i in range(size-1):
            smallIndex = i
            for j in range(i, size):
                barras, j, -1, i, -1
                if barras[j] < barras[smallIndex]:
                    smallIndex = j
            barras[i], barras[smallIndex] = barras[smallIndex], barras[i]
pygame.quit()
