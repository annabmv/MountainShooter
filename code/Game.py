import pygame

from code.Const import WIND_WIDTH, WIND_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
