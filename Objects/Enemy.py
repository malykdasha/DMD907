import pygame
from Objects.Object import ObjectClass
# self.x положение на экране в данный момент времени
# параметр x в конструкторе (__init__)
# это начальное положение на экране в начальный момент времени


class EnemyClass(ObjectClass):
    def __init__(self, x, y, vx, vy, game):
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
        super().__init__(game)

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 200, 200), (self.x, self.y, 50, 50))

    def update(self):
        self.y += self.vy
        if self.x <= 0 or self.x >= self.game.WIDTH - 50:
            self.vx = - self.vx
        self.x += self.vx
