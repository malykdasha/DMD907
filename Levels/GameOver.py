import Objects
import Levels
import pygame
import Handlers


class GameOver(Levels.Level):
    def __init__(self, game):
        super().__init__(game)
        timer = game.objects_dict['timer']
        time = (pygame.time.get_ticks() - timer.start_time) / 1000

        game.clear()

        self.game.add_object(Objects.TextClass(game, 72, 'GAME OVER!', (255, 100, 212), 20, 60))
        self.game.add_object(Objects.TextClass(game, 50, 'Your score is:', (255, 100, 212), 20, 142))
        self.game.add_object(Objects.TextClass(game, 64, str(time), (255, 100, 212), 20, 178))

        exit_handler = Handlers.ExitHandlerClass(game)
        esc_handler = Handlers.EscHandlerClass(game)
        self.game.add_handler(exit_handler)
        self.game.add_handler(esc_handler)

        def start(button):
            button.game.current_level = Levels.MenuLevel(button.game)
        self.game.add_object(Objects.ButtonClass(20, 340, 320, 40, 40, 'Menu', start, game))

        def restart(button):
             if button.game.current_level == Levels.GameLevel1(button.game):
                 game.clear()
                 button.game.current_level = Levels.GameLevel1(button.game)
             elif button.game.current_level == Levels.GameLevel2(button.game):
                 game.clear()
                 button.game.current_level = Levels.GameLevel2(button.game)
             elif button.game.current_level == Levels.GameLevel3(button.game):
                 game.clear()
                 button.game.current_level = Levels.GameLevel3(button.game)

        self.game.add_object(Objects.ButtonClass(20, 383, 320, 40, 40, 'Restart', restart, game))

        sound_of_death = pygame.mixer.Sound('Sources/Sounds/lazha.wav')
        sound_of_death.play()
