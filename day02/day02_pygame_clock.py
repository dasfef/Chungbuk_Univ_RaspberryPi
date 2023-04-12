import pygame
from time import gmtime, strftime

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("Digital Clock")
font = pygame.font.SysFont(None, 72)

while True :
    screen.fill(white)
    currNow = strftime("%H:%M:%S", gmtime())
    text = font.render(currNow, True, (0, 200, 0))
    
    screen.blit(text, (160-text.get_width()//2, 120-text.get_height()//2))
    pygame.display.flip()