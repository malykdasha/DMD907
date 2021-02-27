import pygame
from Player import PlayerClass
from PlayerHandler import PlayerHandlerClass
from ExitHander import ExitHandlerClass
from Spawner import SpawnerClass
# from GameOver import GameOverClass
# я его доделаю и залью
from Health import HealthClass
from random import randint




class GameClass:
    def __init__(self):
        self.WIDTH = 360  # ширина игрового окна
        self.HEIGHT = 480  # высота игрового окна
        self.FPS = 30  # частота кадров в секунду

        # создаем игру и окно
        pygame.init()
        pygame.mixer.init()  # для звука
        pygame.mixer.music.load('PPK - Ressurection .mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("DMD907")
        self.clock = pygame.time.Clock()

        self.PURPURN = (0, 0, 100)

        self.running = True

        self.player = PlayerClass(self)

        self.health = HealthClass(self)

        self.objects = [self.player, self.health]

        player_handler = PlayerHandlerClass(self)
        exit_handler = ExitHandlerClass(self)
        self.handlers = [player_handler, exit_handler]

        self.scripts = [SpawnerClass(self)]

        # self.g = GameOverClass(self)

    def fps(self):
        self.clock.tick(self.FPS)

    def run_scripts(self):
        for script in self.scripts:
            script.run()

    def events(self):
        all_events = pygame.event.get()
        # все события за текущий кадр
        for handler in self.handlers:
            handler.process(all_events)

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        self.screen.fill(self.PURPURN)

        for o in self.objects:
            o.draw()

        pygame.display.flip()

    # def game_over(self):
    #     self.g.run()

    def start(self):
        while self.running:
            self.fps()
            self.run_scripts()
            self.events()
            self.update()
            self.draw()
            # self.game_over()
