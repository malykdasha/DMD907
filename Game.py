import pygame
from Objects.Player import PlayerClass
from Handlers.PlayerHandler import PlayerHandlerClass
from Handlers.ExitHander import ExitHandlerClass
from Scripts.EnemySpawner import SpawnerClass
from Objects.Timer import TimerClass
from Scripts.CheckTouch import CheckTouchClass
from Objects.Health import HealthClass
from Handlers.WeaponHandler import WeaponHandlerClass
from Scripts.WeaponSpawner import WeaponSpawnerClass
from Objects.Button import ButtonClass


class GameClass:
    def __init__(self):
        self.WIDTH = 360  # ширина игрового окна
        self.HEIGHT = 480  # высота игрового окна
        self.FPS = 30  # частота кадров в секунду
        # создаем игру и окно
        pygame.init()
        pygame.font.init()  # для текста!
        pygame.mixer.init()  # для звука
        pygame.mixer.music.load('Sources/PPK - Ressurection .mp3')
        # pygame.mixer.music.load('Sources/8-Bit Universe - Billie Jean.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("DMD907")
        self.clock = pygame.time.Clock()
        self.PURPURN = (0, 0, 100)

        self.is_running = True
        self.is_pause = False

        self.player = PlayerClass(self)
        self.health = HealthClass(self)
        self.timer = TimerClass(self)

        self.objects = [self.player, self.health, self.timer]

        player_handler = PlayerHandlerClass(self)
        weapon_handler = WeaponHandlerClass(self)
        exit_handler = ExitHandlerClass(self)
        self.handlers = [player_handler, weapon_handler, exit_handler]

        self.spawner = SpawnerClass(self)
        self.check_touch = CheckTouchClass(self)
        self.weapon_spawner = WeaponSpawnerClass(self)
        self.scripts = [self.spawner, self.check_touch]

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

    def menu(self):
        while self.is_running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(self.PURPURN)
            start_button = ButtonClass(1, 1, 100, 20, 'sth', self)
            start_button.draw()
            start_button.is_pressed(self.start)
            pygame.display.flip()

    def start(self):
        while self.is_running:
            self.fps()
            self.run_scripts()
            self.events()
            if not self.is_pause:
                self.update()
                self.draw()
            pygame.display.flip()
