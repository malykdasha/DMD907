import pygame
import Handlers


class PlayerHandlerClass(Handlers.HandlerClass):
    def process(self, all_events):
        acceleration = 750
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.game.objects_dict['player'].ax += -acceleration
                if event.key == pygame.K_d:
                    self.game.objects_dict['player'].ax += acceleration
                if event.key == pygame.K_w:
                    self.game.objects_dict['player'].ay += -acceleration
                if event.key == pygame.K_s:
                    self.game.objects_dict['player'].ay += acceleration
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.game.objects_dict['player'].ax -= -acceleration
                if event.key == pygame.K_d:
                    self.game.objects_dict['player'].ax -= acceleration
                if event.key == pygame.K_w:
                    self.game.objects_dict['player'].ay -= -acceleration
                if event.key == pygame.K_s:
                    self.game.objects_dict['player'].ay -= acceleration
