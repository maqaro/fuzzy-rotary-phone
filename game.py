import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("gone huntin'")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

playerX = 512
playerY = 300
enemyX = 0
enemyY = 300

background = pygame.image.load("gameFiles/backdrop.png").convert()
floor = pygame.image.load("gameFiles/floor.png").convert_alpha()
enemy = pygame.image.load("gameFiles/enemy.png").convert_alpha()
player = pygame.image.load("gameFiles/player.png").convert_alpha()
playerRect = player.get_rect(center=(playerX, playerY))
enemyRect = enemy.get_rect(center=(enemyX, enemyY))

movement = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    if enemyRect.left > 1050 or enemyRect.right < 0:
        print("out of bounds")
        direction = random.randint(0, 1)
        yPos = random.randint(50, 400)
        if direction == 0:
            enemyRect.center = (0, yPos)
            movement = 3
        elif direction == 1:
            enemyRect.center = (1000, yPos)
            movement = -3

    screen.blit(background, (0, 0))
    screen.blit(floor, (0, 0))
    enemyRect.x += movement
    screen.blit(enemy, enemyRect)
    screen.blit(player, playerRect)

    if playerRect.colliderect(enemyRect):
        print("collided")

    pygame.display.update()
    clock.tick(60)
