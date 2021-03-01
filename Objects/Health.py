import pygame
from Objects.Object import ObjectClass


class HealthClass(ObjectClass):
    def __init__(self, game):
        self.x = game.WIDTH / 2
        self.y = game.HEIGHT - 20
        self.radius = 10
        self.health = list(range(1, int(11)))
        super().__init__(game)

    def draw(self):
        for i in self.health:
            pygame.draw.circle(self.game.screen, (0, 0, 0), (i * 25, self.y), self.radius)
