import pygame
import os

class Player:
    def __init__(self):
        self.all_animations = ("Idle", "Run")
        self.all_images = []
        for i in range(len(self.all_animations)):
            images = []
            n = len(os.listdir(f"png/player/{self.all_animations[i]}"))
            for j in range(1, n+1):
                img = pygame.image.load(f"png/player/{self.all_animations[i]}/{self.all_animations[i]} ({j}).png")
                img = pygame.transform.scale_by(img, 0.4)
                images.append(img)
            self.all_images.append(images)

        self.frame = 0
        self.animation_index = 0
        self.image = self.all_images[self.animation_index][self.frame]
        self.rect = self.image.get_rect(topleft=(100, 200))
        self.speed = 5
        self.health = 100
        self.ammo = 50
        self.time_change = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def animation(self):
        if pygame.time.get_ticks() - self.time_change >= 100:
            self.time_change = pygame.time.get_ticks()
            self.frame += 1
        if self.frame >= len(self.all_images):
            self.frame = 0
        self.image = self.all_images[self.animation_index][self.frame]

    def move(self):
        pass
