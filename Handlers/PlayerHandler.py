import pygame
import Handlers


class PlayerHandlerClass(Handlers.HandlerClass):
    def process(self, all_events):
        acceleration = 1000
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.game.objects_dict['player'].ax += -acceleration
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.game.objects_dict['player'].ax += acceleration
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.game.objects_dict['player'].ay += -acceleration
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.game.objects_dict['player'].ay += acceleration
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.game.objects_dict['player'].ax -= -acceleration
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.game.objects_dict['player'].ax -= acceleration
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.game.objects_dict['player'].ay -= -acceleration
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.game.objects_dict['player'].ay -= acceleration
