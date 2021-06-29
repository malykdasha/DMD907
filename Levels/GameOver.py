import Objects
import Levels
import pygame


class GameOver(Levels.Level):
    def __init__(self, game):
        super().__init__(game)
        game.clear()
        font = pygame.font.Font(None, 72)
        text_surface = font.render('GAME OVER!', True, (200, 40, 30))
        self.game.add_object(Objects.TextClass(game, text_surface))

        def start(button):
            button.game.current_level = Levels.MenuLevel(button.game)
        self.game.add_object(Objects.ButtonClass(1, 360, 100, 20, 20, 'menu', start, game))
        sound_of_death = pygame.mixer.Sound('Sources/lazha.wav')
        sound_of_death.play()
        pygame.mixer.music.pause()
