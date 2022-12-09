import random
import pygame

from dino_runner.components.power_up.shield import Shield

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))

    def reset_power_ups (self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("Generating power up")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(Shield())
            return self.power_ups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_ups in self.power_ups:
            power_ups.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_ups.rect):
                power_ups.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = power_ups.type
                power_ups.start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = power_ups.start_time + (time_random * 1000)
                self.power_ups.remove(power_ups)

    def draw(self, screen):
        for power_ups in self.power_ups:
            power_ups.draw(screen)
