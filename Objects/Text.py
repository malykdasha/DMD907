import pygame
import Objects


class TextClass(Objects.ObjectClass):
    def __init__(self, game, text_surface):
        super().__init__(game)
        self.text_surface = text_surface

    def draw(self):
        self.game.screen.blit(self.text_surface, (20, 160))
