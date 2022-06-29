import pygame

import config
from game import Game
from game_state import GameState


# start the game
pygame.init()

# create the screen and set the caption
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Baking Game")

# create and set up the game
game = Game(screen)
game.set_up()
frame_rate = pygame.time.Clock()

# create the game loop
while game.game_state == GameState.RUNNING:
    frame_rate.tick(60)
    game.update()
    pygame.display.flip()  # updates the screen
