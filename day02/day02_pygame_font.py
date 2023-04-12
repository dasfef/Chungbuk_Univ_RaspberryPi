import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

pygame.init()
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ex Pygame")

font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Hello Pygame Text", True, (0, 128, 0))
                   
while True :
    screen.fill(white)
    screen.blit(text, (320-text.get_width()//2, 240-text.get_height()//2))
    pygame.display.flip()