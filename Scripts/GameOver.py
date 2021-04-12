import Objects
import Scripts
#d import Levels.GameLevel1
#from Game import GameClass
import pygame


class GameOverClass(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.sound_of_death = pygame.mixer.Sound('Sources/lazha.wav')
        self.font = pygame.font.Font(None, 72)
        self.text_surface = self.font.render('GAME OVER!', True, (255, 0, 0))

        def start():
            pass
        #     b.game.current_level = GameLevel1.GameLevel1()
        self.main_menu = Objects.ButtonClass(1, 360, 100, 20, 20, 'menu', start, game)

    def run(self):
        self.main_menu.draw()
        # sedinmenu.is_pressed(None)
        self.game.screen.blit(self.text_surface, (20, 160))
        self.sound_of_death.play()
        pygame.mixer.music.pause()
        pygame.display.flip()
