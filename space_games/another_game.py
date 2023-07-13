import pygame
import sys
import os
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW1_HIT = pygame.USEREVENT +1
YELLOW2_HIT = pygame.USEREVENT +2
RED_HIT = pygame.USEREVENT +3


max_bullets = 4
vel = 5
bullet_vel =8
FPS = 60
yellow1_movement = vel
yellow2_movement = -vel

WIDTH,HEIGHT = 800,600

YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','spaceship_yellow.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets','spaceship_red.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),180)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption("My second game")
BORDER = pygame.Rect(0,(HEIGHT//2)-5,WIDTH,10)

def handle_yellow_movement(yellow1,yellow2,vel):
    global yellow1_movement
    global yellow2_movement
    yellow1.x+=yellow1_movement
    if yellow1.x == WIDTH - SPACESHIP_WIDTH:
        yellow1_movement = - yellow1_movement
    if yellow1.x == 0:
        yellow1_movement = - yellow1_movement

    yellow2.x += yellow2_movement
    if yellow2.x == 0:
        yellow2_movement= - yellow2_movement
    if yellow2.x == WIDTH - SPACESHIP_WIDTH :
        yellow2_movement= - yellow2_movement

def handle_yellow_bullet(yellow1,yelllow2,yellow1_bullets,yellow2_bullets,red):
    for bullet in yellow1_bullets:
        bullet.y+=bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow1_bullets.remove(bullet)
        elif bullet.y > HEIGHT - bullet.height :
            yellow1_bullets.remove(bullet)
    for bullet in yellow2_bullets:
        bullet.y+=bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow2_bullets.remove(bullet)
        elif bullet.y > HEIGHT - bullet.height :
            yellow2_bullets.remove(bullet)


def handle_red_bullet(red_bullets,red,yellow1,yellow2):
    for bullet in red_bullets:
        bullet.y-=bullet_vel
        if bullet.colliderect(yellow1):
            pygame.event.post(pygame.event.Event(YELLOW1_HIT))
            red_bullets.remove(bullet)



        elif bullet.colliderect(yellow2):
            pygame.event.post(pygame.event.Event(YELLOW2_HIT))
            red_bullets.remove(bullet)
        elif bullet.y < 0 :
            red_bullets.remove(bullet)


def handle_red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x>0:
        red.x-=vel
    if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - SPACESHIP_WIDTH :
        red.x+=vel
    if keys_pressed[pygame.K_UP] and red.y > HEIGHT//2 + BORDER.height//2:
        red.y-=vel
    if keys_pressed[pygame.K_DOWN] and red.y + SPACESHIP_HEIGHT < HEIGHT:
        red.y+=vel
def handle_draw(red,yellow1,yellow2,red_bullets,yellow1_bullets,yellow2_bullets):
    screen.fill((100,100,123))
    screen.blit(SPACE,(0,0))
    screen.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))

    screen.blit(YELLOW_SPACESHIP_IMAGE,(yellow1.x,yellow1.y))
    screen.blit(YELLOW_SPACESHIP_IMAGE,(yellow2.x,yellow2.y))
    pygame.draw.rect(screen,(56,200,56),BORDER)
    for bullet in red_bullets:
        pygame.draw.rect(screen,(255,0,0),bullet)
    for bullet in yellow1_bullets:
        pygame.draw.rect(screen,(255,255,0),bullet)
    for bullet in yellow2_bullets:
        pygame.draw.rect(screen,(255,255,0),bullet)
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    red = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//2,HEIGHT-SPACESHIP_HEIGHT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow1 = pygame.Rect(0,0,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow2 = pygame.Rect(WIDTH-SPACESHIP_WIDTH,0,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets=[]
    yellow1_bullets = []
    yellow2_bullets = []

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(red_bullets)<max_bullets:
                    bullet = pygame.Rect(red.x+SPACESHIP_WIDTH//2 - 2,red.y ,5,10)
                    red_bullets.append(bullet)
                if len(yellow1_bullets)< max_bullets:
                    bullet = pygame.Rect(yellow1.x +SPACESHIP_WIDTH//2-2,yellow1.y,5,10)
                    yellow1_bullets.append(bullet)

                if len(yellow2_bullets)<max_bullets:
                    bullet = pygame.Rect(yellow2.x +SPACESHIP_WIDTH//2-2,yellow2.y,5,10)
                    yellow2_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed,red)
        handle_yellow_movement(yellow1,yellow2,vel)
        handle_yellow_bullet(yellow1,yellow2,yellow1_bullets,yellow2_bullets,red)
        handle_red_bullet(red_bullets,red,yellow1,yellow2)
        handle_draw(red,yellow1,yellow2,red_bullets,yellow1_bullets,yellow2_bullets)

if __name__ == "__main__":

    main()
