import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("gone huntin'")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    pygame.display.update()