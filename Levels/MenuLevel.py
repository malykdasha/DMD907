from Levels.Level import Level
from Objects.Button import ButtonClass
from Levels.GameLevel2 import GameLevel2
from Levels.GameLevel1 import GameLevel1
from Handlers.ExitHander import ExitHandlerClass


class MenuLevel(Level):
    def __init__(self, game):
        super().__init__(game)

        def start(b):
            b.game.current_level = GameLevel1(b.game)
        self.button_start = ButtonClass(10, 10, 100, 100, 'Hello', start, game)
        self.exit_handler = ExitHandlerClass(game)
        self.objects = [self.button_start]
        self.handlers = [self.exit_handler]
        self.scripts = []
