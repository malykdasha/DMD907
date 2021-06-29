import Objects
import pygame


class StarsClass(Objects.ObjectClass):
    def __init__(self, x, y, vy, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy

    def draw(self):
        pygame.draw.circle(self.game.screen, (255, 255, 0), (self.x, self.y), 1)

    def update(self):
        self.y += self.vy / self.game.FPS
