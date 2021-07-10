import pygame

class Rocket:
    def __init__(self, rocket):
        self.wn = rocket.wn
        self.wn_rect = rocket.wn.get_rect()

        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.wn_rect.center

        #Movement
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.wn.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= 1

        if self.moving_down and self.rect.bottom < self.wn_rect.bottom:
            self.rect.y += 1

        if self.moving_right and self.rect.right < self.wn_rect.right:
            self.rect.x += 1

        if self.moving_left and self.rect.x > 0:
            self.rect.x -= 1
