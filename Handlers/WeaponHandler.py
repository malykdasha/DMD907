from Handlers.Handler import HandlerClass
import pygame


class WeaponHandlerClass(HandlerClass):
    def process(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.game.current_level.weapon_spawner.run()
