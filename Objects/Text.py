import pygame
import Objects


class TextClass(Objects.ObjectClass):
    def __init__(self, game, font_size, text, color, x, y):
        super().__init__(game)
        font = pygame.font.Font(None, font_size)
        self.text_surface = font.render(text, True, color)
        self.x = x
        self.y = y

    def draw(self):
        self.game.screen.blit(self.text_surface, (self.x, self.y))
