import Levels
import Objects
import Handlers


class MenuLevel(Levels.Level):
    def __init__(self, game):
        super().__init__(game)
        self.game.clear()

        def start0(button):
            button.game.current_level = Levels.GameLevel2(button.game)

        def exit_function(button):
            self.game.is_running = False

        def start1(button):
            button.game.current_level = Levels.GameLevel(button.game, 1)

        def start2(button):
            button.game.current_level = Levels.GameLevel(button.game, 2)

        def start3(button):
            button.game.current_level = Levels.GameLevel(button.game, 3)

        score = [0]
        # self.game.add_object(Objects.TextClass(game, 20, 'Max score', (0, 250, 80), 120, 5))
        # self.game.add_object(Objects.TextClass(game, 20, str(score[0]), (0, 200, 30), 120, 15))
        button_width = 200
        button_height = 60
        font_size = 50
        left = (game.WIDTH - button_width) / 2
        delta = button_height + 10
        start = 10
        self.game.add_object(Objects.ButtonClass(left, start, button_width, button_height, font_size,
                                                 'Start game', start0, game), 'game start')
        self.game.add_object(Objects.ButtonClass(left, start + delta, button_width, button_height, font_size,
                                                 'Easy', start1, game), 'game start')
        self.game.add_object(Objects.ButtonClass(left, start + 2 * delta, button_width, button_height, font_size,
                                                 'Medium', start2, game), 'game start')
        self.game.add_object(Objects.ButtonClass(left, start + 3 * delta, button_width, button_height, font_size,
                                                 'Hard', start3, game), 'game start')
        self.game.add_object(Objects.ButtonClass(left, start + 4 * delta, button_width, button_height, font_size,
                                                 'Exit game', exit_function, game), 'game start')

        self.game.add_handler(Handlers.ExitHandlerClass(game), 'exit')
