import pygame
from character import Player
pygame.init()
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

my_player = Player()

FPS =  60
clock = pygame.time.Clock()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("pink")
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)
