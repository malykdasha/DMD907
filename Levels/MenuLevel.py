import Levels
import Objects
import Handlers


class MenuLevel(Levels.Level):
    def __init__(self, game):
        super().__init__(game)
        self.game.clear()

        self.game.add_object(Objects.TextClass(game, 33, 'Welcome!', (255, 100, 212), 20, 20))
        self.game.add_object(Objects.TextClass(game, 33, 'Choose your difficulty:', (255, 100, 212), 20, 60))

        def exit_function(button):
            self.game.is_running = False

        def start0(button):
            button.game.current_level = Levels.GameLevel0(button.game)

        def start1(button):
            button.game.current_level = Levels.GameLevel1(button.game)

        def start2(button):
            button.game.current_level = Levels.GameLevel2(button.game)

        def start3(button):
            button.game.current_level = Levels.GameLevel3(button.game)

        button_width = 200
        button_height = 40
        font_size = 40
        left = 20
        delta = button_height + 5
        start = 100

        file = open('score.data', 'w+')
        score = [0] * 4
        for i, line in enumerate(file):
            score[i] = int(line)
        self.game.add_object(Objects.TextClass(game, 30, 'MAX', (255, 100, 212), 245, start))
        self.game.add_object(Objects.TextClass(game, 30, str(score[0]), (255, 100, 212), 250, start + 30))
        self.game.add_object(Objects.TextClass(game, 30, str(score[1]), (255, 100, 212), 250, start + 20 + delta))
        self.game.add_object(Objects.TextClass(game, 30, str(score[2]), (255, 100, 212), 250, start + 20 + 2 * delta))

        self.game.add_object(Objects.ButtonClass(left, start, button_width, button_height, font_size,
                                                 'Easy', start1, game), 'game start1')
        self.game.add_object(Objects.ButtonClass(left, start + delta, button_width, button_height, font_size,
                                                 'Medium', start2, game), 'game start2')
        self.game.add_object(Objects.ButtonClass(left, start + 2 * delta, button_width, button_height, font_size,
                                                 'Hard', start3, game), 'game start3')
        self.game.add_object(Objects.ButtonClass(left, start + 3 * delta, button_width, button_height, font_size,
                                                 'Relax', start0, game), 'game start0')
        self.game.add_object(Objects.ButtonClass(left, start + 4 * delta, button_width, button_height, font_size,
                                                 'Exit game', exit_function, game), 'game exit')

        self.game.add_handler(Handlers.ExitHandlerClass(game), 'exit')
