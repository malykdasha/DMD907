import pygame
import Objects
import Scripts
# self.x положение на экране в данный момент времени
# параметр x в конструкторе (__init__)
# это начальное положение на экране в начальный момент времени


class EnemyClass(Objects.ObjectClass):
    def __init__(self, x, y, vx, vy, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
        self.width = 50
        self.height = 50
        self.scripts.append(Scripts.EnemyWeaponSpawner(self, game))
        self.scripts.append(Scripts.CheckTouchEnemy(self, game))
        self.sound_of_touch = pygame.mixer.Sound('Sources/Запись.wav')

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 200, 200), (self.x, self.y, self.width, self.height))

    def update(self):
        self.y += self.vy / self.game.FPS
        if self.x <= 0 or self.x >= self.game.WIDTH - self.width:
            self.vx = -self.vx
        self.x += self.vx / self.game.FPS
        if self.y >= self.game.HEIGHT:
            self.game.objects.remove(self)
            self.game.objects_dict['health'].remove()
            self.sound_of_touch.play()
