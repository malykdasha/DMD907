import Handlers
import Objects
import pygame


class WeaponHandlerClass(Handlers.HandlerClass):
    def process(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x = self.game.objects_dict['player'].x + self.game.objects_dict['player'].width/2
                    weapon = Objects.WeaponClass(x=x,
                                                 y=self.game.objects_dict['player'].y,
                                                 vy=-700,
                                                 game=self.game)
                    self.game.add_object(weapon)
