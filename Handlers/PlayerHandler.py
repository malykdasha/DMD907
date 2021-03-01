import pygame
from Handlers.Handler import HandlerClass


class PlayerHandlerClass(HandlerClass):
    def process(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.game.player.vx -= 10
                if event.key == pygame.K_d:
                    self.game.player.vx += 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.game.player.vx -= 10
                if event.key == pygame.K_a:
                    self.game.player.vx += 10
