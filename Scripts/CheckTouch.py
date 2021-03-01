import pygame
from Scripts.Script import ScriptClass
from Objects.Enemy import EnemyClass
from Scripts.GameOver import GameOverClass


class CheckTouchClass(ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.sound_of_touch = pygame.mixer.Sound('Sources/Звук_урона_в_Майнкрафт.wav')

    def run(self):
        for enemy in self.game.objects:
            if type(enemy) is EnemyClass:
                if self.game.player.x - 10 <= enemy.x <= self.game.player.x + 40:
                    if self.game.HEIGHT - 50 <= enemy.y <= self.game.HEIGHT - 40:
                        self.game.health.health.pop()
                        self.game.objects.remove(enemy)
                        self.sound_of_touch.play()
                        if len(self.game.health.health) == 0:
                            # pygame.time.wait(4000)
                            # self.game.is_running = False
                            self.game.is_pause = True
                            GameOverClass(self.game).run()
