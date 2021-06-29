import pygame
import Objects


class TextClass(Objects.ObjectClass):
    def __init__(self, game, text_surface, x, y):
        super().__init__(game)
        self.x = x
        self.y = y
        self.text_surface = text_surface

    def draw(self):
        self.game.screen.blit(self.text_surface, (self.x, self.y))
