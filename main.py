import pygame

pygame.init()
import random
WIDTH = 1000
HEIGHT = 640

COLORS = ["black", "white", "purple", "pink"]
current_color = COLORS[0]
index = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                index += 1
                if index >= len(COLORS):
                    index = 0
                current_color = COLORS[index]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                current_color = (r,g,b)

    screen.fill(current_color)
    pygame.display.update()
