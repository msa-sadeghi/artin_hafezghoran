import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("png/player/Idle/Idle (1).png")
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect(topleft=(100, 400))
        self.speed = 5
        self.health = 100
        self.ammo = 50

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.speed




    