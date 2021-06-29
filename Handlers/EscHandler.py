import pygame
import Handlers
import Levels


class EscHandlerClass(Handlers.HandlerClass):
    def process(self, all_events):
        for e in all_events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.game.current_level = Levels.MenuLevel(self.game)
