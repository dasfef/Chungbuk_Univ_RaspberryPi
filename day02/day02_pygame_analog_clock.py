import pygame
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Load Image")
loadImage = pygame.image.load("compass.png").convert()
screen.fill(white)

degree=0
clock = pygame.time.Clock()
FPS = 30

while True:
    rotated = pygame.transform.rotate(loadImage, degree)
    rect = rotated.get_rect()
    rect.center = [256, 256]
    screen.blit(rotated, rect)
    pygame.display.flip()
    degree += 5
    if degree > 360 :
        degree = 0
    clock.tick(FPS)

pygame.quit()