import pygame
import Handlers


class ExitHandlerClass(Handlers.HandlerClass):
    def process(self, all_events):
        for e in all_events:
            # проверить закрытие окна
            if e.type == pygame.QUIT:
                self.game.is_running = False
