import sys
import pygame

from ship import Rocket

class Game:

    def __init__(self):
        pygame.init()
        self.wn = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rocket")

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self.check_events()
            self.rocket.update()
            self.update_screen()

    def update_screen(self):
        self.wn.fill((230, 230, 230))
        self.rocket.blitme()

        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = True

                if event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True

                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True

                if event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False

                if event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False

                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False

                if event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False

if __name__ =='__main__':
    rocket = Game()
    rocket.run_game()
