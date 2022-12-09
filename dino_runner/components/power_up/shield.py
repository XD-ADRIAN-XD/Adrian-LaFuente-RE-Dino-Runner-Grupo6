import random
from dino_runner.utils.constants import SCREEN_HEIGHT

from pygame.sprite import Sprite

from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.power_up.power_up import PowerUp

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Shield, self).__init__(self.image, self.type)