import pygame
from pygame.locals import *
import sys
pygame.init()
screen = pygame.display.set_mode((480,480),0,32)
pygame.display.set_caption("Hello Grids ")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    for x in range(int(screen.get_width()/20)):
        for y in range(int(screen.get_height()/20)):
            if (x+y)%2 == 0:
                pygame.draw.rect(screen,(50,70,123),(x,y,20,20))
            else:
                pygame.draw.rect(screen,(123,50,70),(x,y,20,20))
    pygame.display.update()                            
