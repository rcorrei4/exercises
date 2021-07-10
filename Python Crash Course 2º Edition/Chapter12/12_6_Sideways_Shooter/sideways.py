import sys

import pygame

from ship import Ship
from bullet import Bullet

class Side_Shooter:
    def __init__(self):
        pygame.init()
        self.wn = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Sideways Shooter")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.left <= 0:
                    self.bullets.remove(bullet)

            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True

                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

                if event.key == pygame.K_SPACE:
                    self._fire_bullet()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False

                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        self.wn.fill((230, 230, 230))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__=='__main__':
    sideways = Side_Shooter()
    sideways.run_game()
