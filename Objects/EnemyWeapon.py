import Objects
import Scripts
import pygame


class EnemyWeapon(Objects.ObjectClass):
    def __init__(self, vy, x, y, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy
        self.width = 50
        self.height = 50
        self.img = self.game.bullet_img
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.health = 1
        self.scripts.append(Scripts.CheckTouchEnemy(self, game))

    def draw(self):
        self.game.screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.y += self.vy / self.game.FPS
        if self.y >= self.game.HEIGHT:
            self.game.objects.remove(self)
