import pygame
from Objects.Button import ButtonClass
import Game


class MenuClass:
    def __init__(self):
        menu_background = pygame.image.load('Sources/фон.jpg')
        start_button = ButtonClass(1, 1, 100, 20, 'sth', game=Game.GameClass)
        pygame.display.set_mode((360, 480))
        self.ismenurunning=True
        while self.ismenurunning:
            pygame.display.update()


MenuClass()
