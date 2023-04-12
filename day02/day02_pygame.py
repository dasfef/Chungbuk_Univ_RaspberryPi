import pygame

black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
size = [340, 270]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ex Pygame")

gameExit = False
lead_X = 50
lead_Y = 50

while not gameExit:
    for event in pygame.event.get():
#         print(event)
        
        if event.type == pygame.QUIT :
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_X -= 10
            if event.key == pygame.K_RIGHT:
                lead_X += 10
            if event.key == pygame.K_UP:
                lead_Y -= 10
            if event.key == pygame.K_DOWN:
                lead_Y += 10
            
        screen.fill(white)
        pygame.draw.rect(screen, black, [lead_X, lead_Y, 10, 10])
        pygame.display.flip()
        
pygame.quit()
quit()