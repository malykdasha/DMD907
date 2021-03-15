from Levels.Level import Level
import pygame
from Objects.Button import ButtonClass
from Levels.GameLevel2 import GameLevel2
from Levels.GameLevel1 import GameLevel1
from Handlers.ExitHander import ExitHandlerClass


class MenuLevel(Level):
    def __init__(self, game):
        super().__init__(game)

        def start(b):
            b.game.current_level = GameLevel1(b.game)

        def pause(is_paused):
            is_paused = False
            if not is_paused:
                pygame.mixer.music.pause()
                is_paused = True
            else:
                pygame.mixer.music.unpause()
        self.button_start = ButtonClass(10, 10, 100, 20, 20, 'Start game', start, game)
        self.pause_button = ButtonClass(150, 10, 10, 10, 15, 'II', pause, game)
        self.exit_handler = ExitHandlerClass(game)
        self.objects = [self.button_start, self.pause_button]
        self.handlers = [self.exit_handler]
        self.scripts = []
