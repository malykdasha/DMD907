import Levels
import Objects
import Handlers


class MenuLevel(Levels.Level):
    def __init__(self, game):
        super().__init__(game)
        self.game.clear()

        def start(button):
            button.game.current_level = Levels.GameLevel2(button.game)

        def exit_function(button):
            self.game.is_running = False

        def start1(button):
            button.game.current_level = Levels.GameLevel(button.game, 1)

        def start2(button):
            button.game.current_level = Levels.GameLevel(button.game, 2)

        def start3(button):
            button.game.current_level = Levels.GameLevel(button.game, 3)

        self.game.add_object(Objects.ButtonClass(10, 10, 100, 20, 20, 'Start game', start, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 40, 100, 20, 20, 'Easy', start1, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 70, 100, 20, 20, 'Medium', start2, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 100, 100, 20, 20, 'Hard', start3, game), 'game start')
        self.game.add_object(Objects.ButtonClass(10, 130, 100, 20, 20, 'Exit game', exit_function, game), 'game start')
        self.game.add_handler(Handlers.ExitHandlerClass(game), 'exit')
