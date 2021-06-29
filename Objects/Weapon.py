import Objects
import pygame


class WeaponClass(Objects.ObjectClass):
    def __init__(self, vy, x, y, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy
        self.width = 4
        self.height = 10

    def draw(self):
        pygame.draw.rect(self.game.screen, (255, 201, 247), (self.x, self.y, self.width, self.height))

    def update(self):
        self.y += self.vy / self.game.FPS
