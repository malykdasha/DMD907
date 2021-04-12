import Objects
import Scripts
import Levels


class NextLevel(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        # проверяет всaе ли враги живы, если мертвы, то следующий уровень
        for obj in self.game.objects:
            if type(obj) is Objects.EnemyClass:
                break
        else:
            self.game.current_level = Levels.GameLevel1(self.game, self.game.current_level.count + 1)
