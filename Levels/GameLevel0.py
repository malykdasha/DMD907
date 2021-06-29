import Levels
import Handlers
import Objects
import Scripts


class GameLevel0(Levels.Level):
    def __init__(self, game):
        super().__init__(game)
        self.game.clear()
        player = Objects.PlayerClass(game)
        self.game.add_object(player, 'player')

        player_handler = Handlers.PlayerHandlerClass(game)
        exit_handler = Handlers.ExitHandlerClass(game)
        esc_handler = Handlers.EscHandlerClass(game)
        self.game.add_handler(esc_handler)
        self.game.add_handler(player_handler)
        self.game.add_handler(exit_handler)

        star_spawner = Scripts.StarSpawnerClass(game)
        self.game.add_script(star_spawner)
