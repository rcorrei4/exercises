import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, stars_grid):
        super().__init__()
        self.wn = stars_grid.wn

        self.image = pygame.image.load('../../images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
