from Handlers.Handler import HandlerClass
import pygame


class WeaponHandlerClass(HandlerClass):
    def process(self, all_events):
        for event in all_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.current_level.weapon_spawner.run()
                    # self.game.current_level.weapon.append(weapon)
