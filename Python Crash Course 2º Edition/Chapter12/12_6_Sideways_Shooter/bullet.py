import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, sideways):
        super().__init__()
        self.wn = sideways.wn
        self.color = (60, 60, 60)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midleft = sideways.ship.rect.midleft

    def update(self):
        self.rect.x -= 1

    def draw_bullet(self):
        pygame.draw.rect(self.wn, self.color, self.rect)
