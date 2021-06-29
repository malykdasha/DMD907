import Objects
import pygame


class EnemyWeapon(Objects.ObjectClass):
    def __init__(self, vy, x, y, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy
        self.width = 5
        self.height = 30

    def draw(self):
        pygame.draw.rect(self.game.screen, (255, 31, 0), (self.x, self.y, self.width, self.height))

    def update(self):
        self.y += self.vy / self.game.FPS
        if self.y >= self.game.HEIGHT:
            self.game.objects.remove(self)
