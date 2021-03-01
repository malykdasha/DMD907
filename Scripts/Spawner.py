from Scripts.Script import ScriptClass
from Objects.Enemy import EnemyClass
from Objects.Helper import HelperClass
from random import randint


class SpawnerClass(ScriptClass):
    def __init__(self, game):
        self.tick = 20
        self.time = 0
        super().__init__(game)

    def run(self):
        self.time += 1

        if self.tick > 4 and self.time % 60 == 0:
            self.tick -= 1

        if self.time % self.tick == 0:
            enemy = EnemyClass(randint(0, self.game.WIDTH), -10, randint(1, 20), self.game)
            self.game.objects.append(enemy)
        if self.time % self.tick == 1:
            helper = HelperClass(randint(0, self.game.WIDTH), -10, 5, self.game)
            self.game.objects.append(helper)
