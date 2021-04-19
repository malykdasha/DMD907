from Levels.Level import Level
import pygame
from Objects.Button import ButtonClass
from Handlers.ExitHander import ExitHandlerClass
import Levels.MenuLevel


class SettingsLevel(Level):
    def __init__(self, game):
        super().__init__(game)

        def pause(is_paused):
            is_paused = False
            if not is_paused:
                pygame.mixer.music.pause()
                is_paused = True
            else:
                pygame.mixer.music.unpause()

        def silence(is_silence):
            game.sound_volume = 0

        def back(button):
            button.game.current_level = Levels.MenuLevel.MenuLevel(button.game)
            pass

        self.pause_button = ButtonClass(150, 10, 10, 10, 15, 'II', pause, game)
        self.silence_button = ButtonClass(170, 10, 25, 10, 15, 'Tss', silence, game)
        self.back_button = ButtonClass(40, 40, 100, 25, 15, 'Back to menu', back, game)
        self.exit_handler = ExitHandlerClass(game)
        self.handlers = [self.exit_handler]
        self.objects = [self.silence_button, self.pause_button, self.back_button]