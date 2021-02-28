from Scripts.Script import ScriptClass
from Objects.Enemy import EnemyClass
from random import randint


class SpawnerClass(ScriptClass):
    def __init__(self, game):
        self.tick = 0
        super().__init__(game)

    def run(self):
        self.tick += 1
        if self.tick == 8:
            self.tick = 0

            enemy = EnemyClass(randint(0, self.game.WIDTH), 0, randint(5, 10), self.game)
            self.game.objects.append(enemy)
