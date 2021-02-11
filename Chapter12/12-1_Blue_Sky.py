import sys

import pygame

class Screen:

    def __init__(self):
        pygame.init()
        self.wn = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.wn.fill((0, 0, 255))

            pygame.display.flip()

if __name__=='__main__':
    blue_sky = Screen()
    blue_sky.run_game()
