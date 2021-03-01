from Objects.Object import ObjectClass
import pygame


class HelperClass(ObjectClass):
    def __init__(self, x, y, vy, game):
        self.x = x
        self.y = y
        self.vy = vy
        super().__init__(game)

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y, 10, 10))

    def update(self):
        self.y += self.vy
