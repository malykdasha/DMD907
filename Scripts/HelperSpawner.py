import Objects
import Scripts
from random import randint


class HelperSpawnerClass(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.tick = 20
        self.time = 0

    def run(self):
        self.time += 1

        if self.tick > 15 and self.time % 60 == 0:
            self.tick -= 1

        if self.time % 300 == 0:
            helper = Objects.HelperClass(randint(0, self.game.WIDTH), -10, 200, self.game)
            self.game.add_object(helper)
