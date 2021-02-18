import pygame
from Object import ObjectClass
from Enemy import EnemyClass
# import time для отслеживания задеваний
pygame.mixer.init()
s = pygame.mixer.Sound('Звук_урона_в_Майнкрафт.wav')


class HealthClass(ObjectClass):
    def __init__(self, game):
        self.x = game.WIDTH / 2
        self.y = game.HEIGHT - 20
        self.radius = 10
        self.health = list(range(1, int(10) + 1))
        super().__init__(game)

    def draw(self):
        for i in self.health:
            pygame.draw.circle(self.game.screen, (0, 0, 0), (i * 25, self.y), self.radius)

    def update(self):
        for enemy in self.game.objects:
            if type(enemy) is EnemyClass:
                if self.game.player.x - 10 <= enemy.x <= self.game.player.x + 40:
                    if self.game.HEIGHT - 50 <= enemy.y <= self.game.HEIGHT - 40:
                        # time.sleep(2)
                        if len(self.health) == 1:
                            self.game.running = False
                        else:

                            self.health.pop()
                            self.game.objects.remove(enemy)
                            s.play()
                            