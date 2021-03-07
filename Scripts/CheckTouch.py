import pygame
from Scripts.Script import ScriptClass
from Objects.Enemy import EnemyClass
from Scripts.GameOver import GameOverClass
from Objects.Helper import HelperClass


class CheckTouchClass(ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.sound_of_touch = pygame.mixer.Sound('Sources/Запись.wav')

    def run(self):
        for enemy in self.game.current_level.objects:
            if type(enemy) is EnemyClass:
                if self.game.current_level.player.x - 10 <= enemy.x <= self.game.current_level.player.x + 40:
                    if self.game.HEIGHT - 50 <= enemy.y <= self.game.HEIGHT - 40:
                        self.game.current_level.health.health.pop()
                        self.game.current_level.objects.remove(enemy)
                        self.sound_of_touch.play()
                        if len(self.game.current_level.health.health) == 0:
                            # pygame.time.wait(4000)
                            # self.game.is_running = False
                            self.game.is_pause = True
                            GameOverClass(self.game).run()
            if type(enemy) is HelperClass:
                if self.game.current_level.player.x - 10 <= enemy.x <= self.game.current_level.player.x + 40:
                    if self.game.HEIGHT - 50 <= enemy.y <= self.game.HEIGHT - 40:
                        if len(self.game.current_level.health.health) != 10:
                            self.game.current_level.health.health.append(len(self.game.current_level.health.health) + 1)
                            self.game.current_level.objects.remove(enemy)