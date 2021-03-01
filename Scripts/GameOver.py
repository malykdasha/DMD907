from Scripts.Script import ScriptClass
import pygame


class GameOverClass(ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.sound_of_death = pygame.mixer.Sound('Sources/lazha.wav')
        self.font = pygame.font.Font(None, 72)
        self.text_surface = self.font.render('GAME OVER!', True, (255, 0, 0))

    def run(self):
        self.game.screen.blit(self.text_surface, (20, 160))
        self.sound_of_death.play()
        pygame.mixer.music.pause()
