import pygame
import sys

pygame.init()

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
ball_surf = pygame.Surface((48, 48))
ball = pygame.draw.circle(ball_surf, (128, 128, 64), (24, 24), 24)
ballrect = ball_surf.get_rect()

while True:
    width, height = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball_surf, ballrect)
    pygame.display.flip()
