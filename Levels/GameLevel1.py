from Levels.Level import Level
from Objects.Player import PlayerClass
from Objects.Health import HealthClass
from Objects.Timer import TimerClass
from Handlers.PlayerHandler import PlayerHandlerClass
from Handlers.ExitHander import ExitHandlerClass
from Scripts.CheckTouch import CheckTouchClass
from Handlers.WeaponHandler import WeaponHandlerClass
from Scripts.WeaponSpawner import WeaponSpawnerClass
from Objects.Enemy import EnemyClass
from random import randint


class GameLevel1(Level):
    def __init__(self, game):
        super().__init__(game)
        self.player = PlayerClass(game)
        self.health = HealthClass(game)
        self.timer = TimerClass(game)
        self.enemy = EnemyClass(self.game.WIDTH/2, -10, 2, 0.5, game)
        self.objects = [self.player, self.health, self.timer, self.enemy]
        player_handler = PlayerHandlerClass(game)
        weapon_handler = WeaponHandlerClass(game)
        exit_handler = ExitHandlerClass(game)
        self.handlers = [player_handler, weapon_handler, exit_handler]

        # self.spawner = SpawnerClass(game)
        self.check_touch = CheckTouchClass(game)
        self.weapon_spawner = WeaponSpawnerClass(game)
        self.scripts = [self.check_touch]
