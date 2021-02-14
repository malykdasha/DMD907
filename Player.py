import pygame
from Object import ObjectClass


class PlayerClass(ObjectClass):
    def __init__(self, game):
        self.x = game.WIDTH / 2
        self.y = game.HEIGHT - 50
        self.vx = 0
        super().__init__(game)

    def draw(self):
        pygame.draw.rect(self.game.screen, (204, 102, 102), (self.x, self.y, 40, 20))

    def update(self):
        self.x += self.vx
        if self.x < 0:
            self.x = 0
        if self.x > self.game.WIDTH - 40:
            self.x = self.game.WIDTH - 40
