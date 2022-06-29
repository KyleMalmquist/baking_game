import pygame
import config

# start the game
pygame.init()

# create the screen and set the caption
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Baking Game")

# create the game loop
while True:
    screen.fill(config.BLACK)
    pygame.display.flip()  # updates the screen
