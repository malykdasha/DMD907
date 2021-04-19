import Objects
import Scripts
import pygame


class HelperClass(Objects.ObjectClass):
    def __init__(self, x, y, vy, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy
        self.scripts.append(Scripts.CheckTouchHelper(game))

    def draw(self):
        pygame.draw.rect(self.game.screen, (70, 120, 70), (self.x, self.y, 10, 10))

    def update(self):
        self.y += self.vy / self.game.FPS
        if self.y >= self.game.HEIGHT:
            self.game.objects.remove(self)
