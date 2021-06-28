import pygame
import Levels


class GameClass:
    def __init__(self):
        self.WIDTH = 360  # ширина игрового окна
        self.HEIGHT = 480  # высота игрового окна
        self.FPS = 60  # частота кадров в секунду
        # создаем игру и окно
        pygame.init()
        pygame.font.init()  # для текста!
        pygame.mixer.init()  # для звука
        pygame.mixer.music.load('Sources/PPK - Ressurection .wav')
        #pygame.mixer.music.load('Sources/8-Bit Universe - Billie Jean.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.sc = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("DMD907")
        self.clock = pygame.time.Clock()
        self.PURPURN = (0, 0, 100)

        self.is_running = True
        self.is_pause = True

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
            script.run()
        for o in self.objects:
            o.run_scripts()

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
        self.sc.fill(self.PURPURN)

        for o in self.objects:
            o.draw()

    def start(self):
        self.is_pause = False
        while self.is_running:
            self.fps()
            self.run_scripts()
            self.events()
            if not self.is_pause:
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