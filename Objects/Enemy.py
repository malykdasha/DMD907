import pygame
import Objects
import Scripts
from random import randint
# self.x положение на экране в данный момент времени
# параметр x в конструкторе (__init__)
# это начальное положение на экране в начальный момент времени


class EnemyClass(Objects.ObjectClass):
    def __init__(self, x, y, vx, vy, game, health):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
        self.width = 80
        self.height = 40
        self.scripts.append(Scripts.EnemyWeaponSpawner(self, game))
        self.scripts.append(Scripts.CheckTouchEnemy(self, game))
        self.sound_of_touch = self.game.sound_of_touch
        self.img = self.game.nlo_img
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

        self.health = health

    def draw(self):
        self.game.screen.blit(self.img, (self.x, self.y))
        # pygame.draw.rect(self.game.screen, (200, 200, 200), (self.x, self.y, self.width, self.height))

    def update(self):
        self.y += self.vy / self.game.FPS
        if self.x <= 0 or self.x >= self.game.WIDTH - self.width:
            self.vx = -self.vx
        self.x += self.vx / self.game.FPS
        if self.y >= self.game.HEIGHT:
            self.game.objects.remove(self)
            self.sound_of_touch.play()
            if self.game.objects_dict['health'].remove():
                return True
