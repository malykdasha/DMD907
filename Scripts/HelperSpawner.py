from Scripts.Script import ScriptClass
from Objects.Helper import HelperClass
from random import randint


class HelperSpawnerClass(ScriptClass):
    def __init__(self, game):
        self.tick = 20
        self.time = 0
        super().__init__(game)

    def run(self):
        self.time += 1

        if self.tick > 15 and self.time % 60 == 0:
            self.tick -= 1

        if self.time % 60 == 0:
            helper = HelperClass(randint(0, self.game.WIDTH), -10, 5, self.game)
            self.game.current_level.objects.append(helper)
