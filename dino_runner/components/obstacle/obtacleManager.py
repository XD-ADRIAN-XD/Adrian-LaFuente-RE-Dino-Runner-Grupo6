import pygame

from dino_runner.components.obstacle.captus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class obstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Captus(SMALL_CAMPTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw

