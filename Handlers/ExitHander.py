import pygame
from Handlers.Handler import HandlerClass


class ExitHandlerClass(HandlerClass):
    def process(self, all_events):
        for e in all_events:
            # проверить закрытие окна
            if e.type == pygame.QUIT:
                self.game.is_running = False
