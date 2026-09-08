import pygame
import random
pygame.init()
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Rect(50, 50, 50, 50)
x = random.randint(50, 950)
y = random.randint(50, 600)
coin = pygame.Rect(x, y, 20, 20)
f = pygame.font.SysFont("Arial", 22)

pick_sound = pygame.mixer.Sound("pick.wav")
mouse_image = pygame.image.load("Martin-Berube-Flat-Animal-Mouse.256 (1).png")
mouse_image = pygame.transform.scale_by(mouse_image, 0.5)
mouse_rect = mouse_image.get_rect(topleft=(100, 300))

score = 0
FPS =  60
clock = pygame.time.Clock()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("pink")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    if player.colliderect(coin):
        coin.x = random.randint(50, 950)
        coin.y = random.randint(50, 600)
        score+=1
        pick_sound.play()
    score_text = f.render(f"score: {score}", True, "red")
    screen.blit(score_text,  (10, 10))
    pygame.draw.rect(screen, "red", player)
    pygame.draw.ellipse(screen, "gold", coin)
    screen.blit(mouse_image, mouse_rect)
    pygame.display.update()
    clock.tick(FPS)
