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
from Scripts.EnemyWeaponSpawner import EnemyWeaponSpawner
from Scripts.StarSpawner import StarSpawnerClass
import Game
from Objects.Weapon import WeaponClass


class GameLevel2(Level):
    def __init__(self, game):
        super().__init__(game)
        self.player = PlayerClass(game)
        self.health = HealthClass(game)
        self.timer = TimerClass(game)
        self.weapon = []
        self.enemy_weapon = []
        self.objects = [self.player, self.health, self.timer] + self.weapon + self.enemy_weapon

        player_handler = PlayerHandlerClass(game)
        weapon_handler = WeaponHandlerClass(game)
        exit_handler = ExitHandlerClass(game)
        self.handlers = [player_handler, weapon_handler, exit_handler]

        self.enemy_spawner = EnemySpawnerClass(game)
        self.helper_spawner = HelperSpawnerClass(game)

        self.check_touch = CheckTouchClass(game)
        self.weapon_spawner = WeaponSpawnerClass(game)
        self.enemy_weapon_spawner = EnemyWeaponSpawner(game)
        self.star_spawner = StarSpawnerClass(game)
        self.scripts = [self.enemy_spawner, self.helper_spawner, self.check_touch, self.enemy_weapon_spawner,
        self.star_spawner]
