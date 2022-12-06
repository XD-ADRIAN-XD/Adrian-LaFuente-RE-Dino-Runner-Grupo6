import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT ,SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obtacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
    
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
    
    def events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
       user_imput = pygame.key.get_pressed()
       self.player.update(user_imput)
       self.obstacle

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        sel.draw_background()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG,(self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG,(image_width + self.x_pos_bg, self.y_pos_bg))