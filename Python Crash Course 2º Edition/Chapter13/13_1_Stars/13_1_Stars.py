import sys
import pygame

from star import Star

class Stars:

    def __init__(self):
        pygame.init()
        self.wn = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stars Grid")

        self.stars = pygame.sprite.Group()
        self._create_grid()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.wn.fill((0, 0, 0))
            self.stars.draw(self.wn)

            pygame.display.flip()

    def _create_grid(self):
        star = Star(self)
        self.stars.add(star)

if __name__ == '__main__':
    stars_grid = Stars()
    stars_grid.run_game()
