import Objects
import Scripts
from random import randint


class EnemySpawnerClass(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.tick = 20
        self.time = 0

    def run(self):
        self.time += 1

        if self.tick > 15 and self.time % 60 == 0:
            self.tick -= 1

        if self.time % 50 == 0:
            enemy = Objects.EnemyClass(x=randint(0, self.game.WIDTH * 0.5), y=-10, vx=300, vy=randint(20, 40), game=self.game)
            self.game.add_object(enemy)
