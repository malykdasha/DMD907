import Levels
import Objects
import Handlers


class MenuLevel(Levels.Level):
    def __init__(self, game):
        super().__init__(game)

        def start(button):
            button.game.current_level = Levels.GameLevel(button.game, 3)
        self.game.add_object(Objects.ButtonClass(10, 10, 100, 20, 20, 'Start game', start, game), 'game start')
        self.game.add_handler(Handlers.ExitHandlerClass(game), 'exit')
