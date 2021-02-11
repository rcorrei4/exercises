import pygame

class Ship:
    def __init__(self, sideways):
        self.wn = sideways.wn
        self.wn_rect = sideways.wn.get_rect()

        self.image = pygame.image.load('../../images/sideways_ship.png')
        self.rect = self.image.get_rect()

        self.rect.midright = self.wn_rect.midright

        #Movement
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.wn.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1

        if self.moving_down and self.rect.bottom < self.wn_rect.bottom:
            self.rect.y += 1
