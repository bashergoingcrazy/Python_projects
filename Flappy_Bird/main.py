import pygame
import random
import sys

pygame.init()
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 480
FPS = 40
d = 8
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
pygame.display.set_caption("FLAPPY TRY ~ !!")

vel = 10
CYLINDER_WIDTH = 20

def drawer(bird):
    screen.fill((255,255,0))
    pygame.draw.circle(screen,(0,2,255),(bird.x,bird.y),20)
    pygame.display.update()


def bird_movement(bird):
    global vel

    bird.y += d


def cylinder():
    cill = pygame.Rect(640,0,CYLINDER_WIDTH,random.randint(0,SCREEN_HEIGHT))
    cill.x -= 3
    pygame.draw.rect(screen,(0,255,0),cill)
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    speed = 120
    bird = pygame.Rect(SCREEN_WIDTH/10,SCREEN_HEIGHT/2,10,10)

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    bird.y-=100


        pygame.time.set_timer(cylinder(),2000)
        bird_movement(bird)
        drawer(bird)
main()
