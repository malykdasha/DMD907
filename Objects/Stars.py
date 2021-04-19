import Objects
import pygame


class HelperClass(Objects.ObjectClass):
    def __init__(self, x, y, vy, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y, 10, 10))

    def update(self):
        self.y += self.vy / self.game.FPS
