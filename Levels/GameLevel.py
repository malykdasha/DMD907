import Levels
import Handlers
import Objects
import Scripts


class GameLevel(Levels.Level):
    def __init__(self, game, count=1):
        super().__init__(game)
        self.count = count
        self.game.clear()
        player = Objects.PlayerClass(game)
        health = Objects.HealthClass(game)
        timer = Objects.TimerClass(game)
        self.game.add_object(player, 'player')
        self.game.add_object(health, 'health')
        self.game.add_object(timer, 'timer')

        player_handler = Handlers.PlayerHandlerClass(game)
        weapon_handler = Handlers.WeaponHandlerClass(game)
        exit_handler = Handlers.ExitHandlerClass(game)
        esc_handler = Handlers.EscHandlerClass(game)
        self.game.add_handler(esc_handler)
        self.game.add_handler(player_handler)
        self.game.add_handler(weapon_handler)
        self.game.add_handler(exit_handler)

        helper_spawner = Scripts.HelperSpawnerClass(game)
        self.game.add_script(helper_spawner)
        next_level = Scripts.NextLevel(game)
        self.game.add_script(next_level)
        star_spawner = Scripts.StarSpawnerClass(game)
        self.game.add_script(star_spawner)
        self.game.current_level = Levels.GameLevel1(game)
