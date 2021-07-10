import pygame
import sys

pygame.init()
wn = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)

    pygame.display.flip()
