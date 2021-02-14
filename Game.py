import pygame
from Enemy import EnemyClass
from Player import PlayerClass
from PlayerHandler import PlayerHandlerClass
from ExitHander import ExitHandlerClass
from Spawner import SpawnerClass


class GameClass:
    def __init__(self):
        self.WIDTH = 360  # ширина игрового окна
        self.HEIGHT = 480  # высота игрового окна
        self.FPS = 30  # частота кадров в секунду

        # создаем игру и окно
        pygame.init()
        pygame.mixer.init()  # для звука
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("DMD907")
        self.clock = pygame.time.Clock()

        self.PURPURN = (255, 204, 204)

        self.running = True
        enemy1 = EnemyClass(50, 0, 10, self)
        enemy2 = EnemyClass(150, 0, 5, self)
        enemy3 = EnemyClass(250, 0, 3, self)

        self.player = PlayerClass(self)

        self.objects = [enemy1, enemy2, enemy3, self.player]

        player_handler = PlayerHandlerClass(self)
        exit_handler = ExitHandlerClass(self)
        self.handlers = [player_handler, exit_handler]

        self.scripts = [SpawnerClass(self)]


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

    def start(self):
        while self.running:
            self.fps()
            self.run_scripts()
            self.events()
            self.update()
            self.draw()
