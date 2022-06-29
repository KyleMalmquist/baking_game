import pygame
import config
from player import Player
from game_state import GameState


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []

    def set_up(self):
        player = Player(1, 1)  # position the player starts at
        self.player = player
        self.objects.append(player)
        print("do set-up")
        self.game_state = GameState.RUNNING

        self.load_map("01")

    def update(self):
        self.screen.fill(config.BLACK)
        print("update")
        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:  # objects must have a render class to be properly rendered
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():

            # exits the game
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED

                # moves the player using WASD
                elif event.key == pygame.K_w:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_a:
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_s:
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_d:
                    self.player.update_position(1, 0)

    def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line), 2,):  # -1 to account for blank line at the end of the map file
                    tiles.append(line[i])

                self.map.append(tiles)

            print(self.map)

    def render_map(self, screen):
        y_position = 0
        for line in self.map:
            x_position = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_position * config.SCALE, y_position * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_position = x_position + 1

            y_position = y_position + 1


map_tile_image = {
    "G" : pygame.transform.scale(pygame.image.load('imgs/grass1.png'), (config.SCALE, config.SCALE)),
    "W" : pygame.transform.scale(pygame.image.load('imgs/water.png'), (config.SCALE, config.SCALE))
}
