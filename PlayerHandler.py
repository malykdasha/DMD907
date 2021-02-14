import pygame
from Handler import HandlerClass


class PlayerHandlerClass(HandlerClass):
    def process(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.player.vx = -10
                if event.key == pygame.K_RIGHT:
                    self.game.player.vx = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.game.player.vx = 0
