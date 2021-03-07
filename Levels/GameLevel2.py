from Levels.Level import Level
from Objects.Player import PlayerClass
from Objects.Health import HealthClass
from Objects.Timer import TimerClass
from Handlers.PlayerHandler import PlayerHandlerClass
from Handlers.ExitHander import ExitHandlerClass
from Scripts.EnemySpawner import EnemySpawnerClass
from Scripts.HelperSpawner import HelperSpawnerClass
from Scripts.CheckTouch import CheckTouchClass
from Handlers.WeaponHandler import WeaponHandlerClass
from Scripts.WeaponSpawner import WeaponSpawnerClass


class GameLevel2(Level):
    def __init__(self, game):
        super().__init__(game)
        self.player = PlayerClass(game)
        self.health = HealthClass(game)
        self.timer = TimerClass(game)

        self.objects = [self.player, self.health, self.timer]
        player_handler = PlayerHandlerClass(game)
        weapon_handler = WeaponHandlerClass(game)
        exit_handler = ExitHandlerClass(game)
        self.handlers = [player_handler, weapon_handler, exit_handler]

        self.enemy_spawner = EnemySpawnerClass(game)
        self.helper_spawner = HelperSpawnerClass(game)

        self.check_touch = CheckTouchClass(game)
        self.weapon_spawner = WeaponSpawnerClass(game)
        self.scripts = [self.enemy_spawner, self.helper_spawner, self.check_touch]
