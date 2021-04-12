import pygame
import Objects
import Scripts


class PlayerClass(Objects.ObjectClass):
    def __init__(self, game):
        super().__init__(game)
        self.x = game.WIDTH / 2
        self.y = game.HEIGHT - 50
        self.vx = 0
        self.vy = 0
        self.width = 40
        self.height = 20
        self.max_v = 500
        self.a = 150
        self.ax = 0
        self.ay = 0
        self.scripts.append(Scripts.CheckTouchClass(game))

    def draw(self):
        pygame.draw.rect(self.game.screen, (204, 102, 102), (self.x, self.y, self.width, self.height))

    def update(self):
        self.vx += self.ax / self.game.FPS
        if self.vx < 0:
            self.vx += self.a / self.game.FPS
        else:
            self.vx -= self.a / self.game.FPS
        self.vy += self.ay / self.game.FPS
        if self.vy < 0:
            self.vy += self.a / self.game.FPS
        else:
            self.vy -= self.a / self.game.FPS

        self.x += self.vx / self.game.FPS
        if self.vx >= self.max_v:
            self.vx = self.max_v
        if self.vx <= - self.max_v:
            self.vx = - self.max_v

        self.y += self.vy / self.game.FPS
        if self.vy >= self.max_v:
            self.vy = self.max_v
        if self.vy <= - self.max_v:
            self.vy = - self.max_v

        if self.x < 0:
            self.x = 0
            self.vx = 0
        if self.x > self.game.WIDTH - self.width:
            self.x = self.game.WIDTH - self.width
            self.vx = 0
        if self.y < 0:
            self.y = 0
            self.vy = 0
        if self.y > self.game.HEIGHT - self.height:
            self.y = self.game.HEIGHT - self.height
            self.vy = 0
