import Objects
import Scripts
from random import randint


class EnemySpawnerClass(Scripts.ScriptClass):
    def __init__(self, game, speed_x, speed_y, health):
        super().__init__(game)
        self.tick = 20
        self.time = 0
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.health = health

    def run(self):
        self.time += 1

        if self.tick > 15 and self.time % 60 == 0:
            self.tick -= 1

        if self.time % 50 == 0:
            enemy = Objects.EnemyClass(x=randint(30, self.game.WIDTH * 0.5), y=-self.speed_y,
                                       vx=self.speed_x, vy=randint(20, 40), game=self.game, health=self.health)
            self.game.add_object(enemy)
