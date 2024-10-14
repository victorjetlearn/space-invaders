import pygame
import os

pygame.init()
width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("space invader game")
velocity = 5
fps = 60
bullet_velocity = 7



background = pygame.transform.scale(pygame.image.load (os.path.join("background.png")),(width,height))
ship1 = pygame.image.load(os.path.join("ship1.png"))
ship1red = pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),90)
ship2 = pygame.image.load(os.path.join("ship2.png"))
ship2yellow = pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)),270)

def drawwindow(red,yellow,red_bullets,yellow_bullets):
    screen.blit(background,(0,0))
    screen.blit(ship1red,(100,height/2))
    screen.blit(ship2yellow,(850,height/2))
    for i in red_bullets:
        pygame.draw.rect(screen, "red")
    for i in yellow_bullets:
        pygame.draw.rect(screen, "yellow")

    pygame.display.update()

def yellow_ship_mov(key_press, yellow):
    if key_press[pygame.K_LEFT]:
        yellow.x -= velocity
    if key_press[pygame.K_RIGHT]:
        yellow.x += velocity
    if key_press[pygame.K_UP]:
        yellow.y -= velocity
    if key_press[pygame.K_DOWN]:
        yellow.y += velocity

def red_ship_mov(key_press, red):
    if key_press[pygame.K_a]:
        red.x -= velocity
    if key_press[pygame.K_d]:
        red.x += velocity
    if key_press[pygame.K_w]:
        red.y -= velocity
    if key_press[pygame.K_s]:
        red.y += velocity

def main():
    red = pygame.Rect(100,300,60,40)
    yellow = pygame.Rect(700,300,60,40)

    red_bullets = []
    yellow_bullets = []

    while True:
            
        for i in pygame.event.get():
                
            if i.type == pygame.QUIT:
                    pygame.quit()



            if i.type == pygame.KEYDOWN:
                if pygame.key== pygame.K_LSHIFT:
                    bullet = pygame.Rect(red.x + red.width, red.height// 2 -2, 10,5)
                    red_bullets.append(bullet)
                if pygame.key== pygame.K_RSHIFT:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.height// 2 -2, 10,5)
                    yellow_bullets.append(bullet)
        key_press = pygame.key.get_pressed()
        red_ship_mov(key_press, red)
        yellow_ship_mov(key_press, yellow)
        drawwindow(red,yellow,red_bullets,yellow_bullets)
    main()
if __name__ == "__main__":
    main()

            


