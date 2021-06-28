import Levels
import Objects
import Handlers


class MenuLevel(Levels.Level):
    def __init__(self, game):
        super().__init__(game)

        def start(button):
            button.game.current_level = Levels.GameLevel(button.game, 1)

        def exit(button):
            self.game.is_running = False

        def start1(button):
            button.game.current_level = Levels.GameLevel(button.game, 1)

        def start2(button):
            button.game.current_level = Levels.GameLevel(button.game, 2)

        def start3(button):
            button.game.current_level = Levels.GameLevel(button.game, 3)

        self.game.add_object(Objects.ButtonClass(10, 10, 100, 20, 20, 'Start game', start, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 40, 100, 20, 20, 'Start level 1', start1, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 70, 100, 20, 20, 'Start level 2', start2, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 100, 100, 20, 20, 'Start level 3', start3, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 130, 100, 20, 20, 'Exit game', exit, game), 'game start')
        self.game.add_handler(Handlers.ExitHandlerClass(game), 'exit')
