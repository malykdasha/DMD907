import pygame
import Levels
from random import randint
import sys


class GameClass:
    def __init__(self):
        self.WIDTH = 1000  # ширина игрового окна
        self.HEIGHT = 800  # высота игрового окна
        self.FPS = 60  # частота кадров в секунду
        # создаем игру и окно
        pygame.init()
        pygame.font.init()  # для текста!
        pygame.mixer.init()  # для звука
        pygame.mixer.music.load('Sources/Sounds/PPK - Ressurection .wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.sound_of_touch = pygame.mixer.Sound('Sources/Sounds/Запись.wav')
        self.org_screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = self.org_screen.copy()
        self.delta_x = 0
        self.delta_y = 0
        self.shake_ticks = 0
        pygame.display.set_caption("DMD907")
        self.clock = pygame.time.Clock()
        self.PURPURN = (0, 0, 100)
        self.nlo_img = pygame.image.load('Sources/Images/nlo.png').convert_alpha()
        self.bullet_img = pygame.image.load('Sources/Images/bullet.png').convert_alpha()
        self.background_image = pygame.image.load('Sources/Images/фон.jpg').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))
        self.is_running = True

        file = open('score.data', 'r+')
        self.score = [0] * 3
        for i, line in enumerate(file):
            self.score[i] = float(line)
        file.close()

        self.objects = []
        self.objects_dict = {}
        self.scripts = []
        self.scripts_dict = {}
        self.handlers = []
        self.handlers_dict = {}

        self.current_level = Levels.MenuLevel(self)

    def add_object(self, obj, name: str = ''):
        self.objects.append(obj)
        if name:
            self.objects_dict[name] = obj

    def add_handler(self, handler, name: str = ''):
        self.handlers.append(handler)
        if name:
            self.handlers_dict[name] = handler

    def add_script(self, script, name: str = ''):
        self.scripts.append(script)
        if name:
            self.scripts_dict[name] = script

    def fps(self):
        self.clock.tick(self.FPS)

    def run_scripts(self):
        for script in self.scripts:
            if script.run():
                return
        for o in self.objects:
            if o.run_scripts():
                return

    def events(self):
        all_events = pygame.event.get()
        # все события за текущий кадр
        for handler in self.handlers:
            handler.process(all_events)

    def update(self):
        for o in self.objects:
            if o.update():
                break

    def draw(self):
        self.screen.fill(self.PURPURN)
        self.screen.blit(self.background_image, (0, 0))

        for o in self.objects:
            o.draw()
        if self.shake_ticks > 0:
            self.shake_ticks -= 1
            if self.shake_ticks % 5 == 0:
                self.delta_x = randint(-10, 10)
                self.delta_y = randint(-10, 10)
        else:
            self.delta_x = 0
            self.delta_y = 0
        self.org_screen.blit(self.screen, (self.delta_x, self.delta_y))

    def start(self):
        while self.is_running:
            self.fps()
            self.run_scripts()
            self.events()
            self.update()
            self.draw()
            pygame.display.flip()

    def clear(self):
        self.objects.clear()
        self.objects_dict.clear()
        self.handlers.clear()
        self.handlers_dict.clear()
        self.scripts.clear()
        self.scripts_dict.clear()
