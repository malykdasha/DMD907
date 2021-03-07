import pygame
from Objects.Button import ButtonClass
from Levels.MenuLevel import MenuLevel


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
        pygame.display.set_caption("DMD907")
        self.clock = pygame.time.Clock()
        self.PURPURN = (0, 0, 100)

        self.is_running = True
        self.is_pause = True

        self.current_level = MenuLevel(self)

    def fps(self):
        self.clock.tick(self.FPS)

    def run_scripts(self):
        for script in self.current_level.scripts:
            script.run()

    def events(self):
        all_events = pygame.event.get()
        # все события за текущий кадр
        for handler in self.current_level.handlers:
            handler.process(all_events)

    def update(self):
        for o in self.current_level.objects:
            o.update()

    def draw(self):
        self.screen.fill(self.PURPURN)

        for o in self.current_level.objects:
            o.draw()

    def menu(self):
        while self.is_running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(self.PURPURN)
            start_button = ButtonClass(1, 150, 100, 20, 'self', self)
            end_button = ButtonClass(259, 150, 100, 20, 'self', self)
            start_button.draw()
            start_button.write(24, 'Start game')
            end_button.draw()
            end_button.write(24, 'Quit game')
            start_button.is_pressed(self.start)
            end_button.is_pressed(self.end)
            pygame.display.flip()

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

    def end(self):
        self.is_running = False
