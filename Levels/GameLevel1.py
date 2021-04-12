import Levels
import Objects


class GameLevel1(Levels.Level):
    def __init__(self, game, count=1):
        super().__init__(game)
        self.count = count
        if count == 1:
            # spawn enemy
            enemy = Objects.EnemyClass((self.game.WIDTH / 2 - 20) % self.game.WIDTH,
                                       -10,
                                       200 * (-1), 20, game)
            self.game.add_object(enemy)
        elif count == 2:
            for i in range(4):
                enemy = Objects.EnemyClass((self.game.WIDTH / 2 - 20 * i) % self.game.WIDTH,
                                           -10 - 10 * i,
                                           200 * (-1) ** i, 20, game)
                self.game.add_object(enemy)
        elif count == 3:
            enemy = Objects.EnemyClass((self.game.WIDTH / 2 - 20) % self.game.WIDTH,
                                       -10 - 100,
                                       200 * (-1), 200, game)
            self.game.add_object(enemy)
