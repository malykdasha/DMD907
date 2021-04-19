import pygame
import Handlers


class PlayerHandlerClass(Handlers.HandlerClass):
    def process(self, all_events):
        acceleration = 1000
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.objects_dict['player'].ax += -acceleration
                if event.key == pygame.K_RIGHT:
                    self.game.objects_dict['player'].ax += acceleration
                if event.key == pygame.K_UP:
                    self.game.objects_dict['player'].ay += -acceleration
                if event.key == pygame.K_DOWN:
                    self.game.objects_dict['player'].ay += acceleration
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.game.objects_dict['player'].ax -= -acceleration
                if event.key == pygame.K_RIGHT:
                    self.game.objects_dict['player'].ax -= acceleration
                if event.key == pygame.K_UP:
                    self.game.objects_dict['player'].ay -= -acceleration
                if event.key == pygame.K_DOWN:
                    self.game.objects_dict['player'].ay -= acceleration
