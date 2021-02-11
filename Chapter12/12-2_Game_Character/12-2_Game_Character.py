import sys

import pygame

class Game:

    def __init__(self):
        pygame.init()
        self.wn = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game Character")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.wn.fill((230, 230, 230))
            pygame.display.flip()

if __name__=='__main__':
    game_character = Game()
    game_character.run_game()
