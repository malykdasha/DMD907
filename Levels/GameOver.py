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

        self.game.add_object(Objects.TextClass(game, 72, 'GAME OVER!', (200, 40, 30), 20, 160))
        self.game.add_object(Objects.TextClass(game, 72, str(time), (200, 40, 30), 50, 300))

        exit_handler = Handlers.ExitHandlerClass(game)
        esc_handler = Handlers.EscHandlerClass(game)
        self.game.add_handler(exit_handler)
        self.game.add_handler(esc_handler)

        def start(button):
            button.game.current_level = Levels.MenuLevel(button.game)
        self.game.add_object(Objects.ButtonClass(1, 360, 100, 20, 20, 'menu', start, game))

        sound_of_death = pygame.mixer.Sound('Sources/lazha.wav')
        sound_of_death.play()
