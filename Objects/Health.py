import pygame
import Objects
import Scripts


class HealthClass(Objects.ObjectClass):
    def __init__(self, game):
        self.x = game.WIDTH / 2
        self.y = game.HEIGHT - 20
        self.radius = 10
        self.value = 10
        super().__init__(game)

    def add(self):
        if self.value != 10:
            self.value += 1

    def remove(self):
        self.value -= 1
        if self.value == 0:
            self.game.is_pause = True
            Scripts.GameOverClass(self.game).run()

    def draw(self):
        for i in range(self.value):
            pygame.draw.circle(self.game.screen, (0, 0, 0), ((i + 1) * 25, self.y), self.radius)
