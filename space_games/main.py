import pygame
import sys
import os
pygame.font.init()
pygame.mixer.init()


WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption("First Space Game!")
BORDER = pygame.Rect((WIDTH//2)-5,0,10,HEIGHT)
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
FPS = 60
vel = 5
WHITE = (255,255,255)
bullet_vel = 7
max_bullets= 3

#BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
#BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',40)

YELLOW_HIT= pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDTH,HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(red,yellow,yellow_bullets,red_bullets,red_health,yellow_health):

    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,(0,0,0),BORDER)
    red_health_text = HEALTH_FONT.render("HEALTH : "+ str(red_health),1,(255,255,255))
    yellow_health_text = HEALTH_FONT.render("HEALTH : "+ str(yellow_health),1,(255,255,255))
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,(255,255,0),bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN,(255,0,0),bullet)
    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
        if keys_pressed[pygame.K_a] and yellow.x >0:#LEFT
            yellow.x-=vel
        if keys_pressed[pygame.K_d] and yellow.x+SPACESHIP_WIDTH < BORDER.x:
            yellow.x+=vel
        if keys_pressed[pygame.K_w] and yellow.y >0:
            yellow.y-=vel
        if keys_pressed[pygame.K_s] and yellow.y+ yellow.height +vel < HEIGHT-12:
            yellow.y+=vel

def red_handle_movement(keys_pressed,red):
        if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x +BORDER.width :#LEFT
            red.x-=vel
        if keys_pressed[pygame.K_RIGHT] and red.x+vel +red.width < WIDTH :
            red.x+=vel
        if keys_pressed[pygame.K_UP]and red.y - vel > 0:
            red.y-=vel
        if keys_pressed[pygame.K_DOWN] and red.y +vel +red.height < HEIGHT - 15:
            red.y+=vel

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x-=bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0 :
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,(255,255,255))
    WIN.blit(draw_text,(WIDTH//2 - draw_text.get_width()//2,HEIGHT/2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(8000)


def main():
    clock = pygame.time.Clock()
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    bullets_red = []
    bullets_yellow = []
    red_health = 20
    yellow_health = 10
    winner_text=""
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bullets_yellow)< max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2 -2 , 10,5)
                    bullets_yellow.append(bullet)
                    #BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(bullets_red)<max_bullets:
                    bullet = pygame.Rect(red.x,red.y +red.height//2 - 2,10,5)
                    bullets_red.append(bullet)
                    #BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health-=1
                #BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health-=1
                #BULLET_HIT_SOUND.play()



        if red_health<=0:
            winner_text = "Yellow Wins!"
        if yellow_health<=0:
            winner_text = "Red Wins!"

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        handle_bullets(bullets_yellow,bullets_red,yellow,red)

        draw_window(red,yellow,bullets_yellow,bullets_red,red_health,yellow_health)
        if winner_text !="":
            draw_winner(winner_text)
            break

    main()


if __name__ == "__main__":

    main()
