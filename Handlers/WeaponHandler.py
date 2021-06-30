import Handlers
import Objects
import pygame


class WeaponHandlerClass(Handlers.HandlerClass):
    def __init__(self, game):
        super().__init__(game)
        self.ticks = 0

    def process(self, all_events):
        if self.ticks:
            self.ticks -= 1
        else:
            for event in all_events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ticks += 10
                        x = self.game.objects_dict['player'].x + self.game.objects_dict['player'].width/2
                        time = (pygame.time.get_ticks() - self.game.objects_dict['timer'].start_time) / 1000
                        if 20 < time < 40 or 60 < time < 80:
                            weapon1 = Objects.WeaponClass(x=x - 30, y=self.game.objects_dict['player'].y,
                                                          vy=-700, game=self.game)
                            weapon2 = Objects.WeaponClass(x=x, y=self.game.objects_dict['player'].y,
                                                          vy=-700, game=self.game)
                            weapon3 = Objects.WeaponClass(x=x + 30, y=self.game.objects_dict['player'].y,
                                                          vy=-700, game=self.game)
                            self.game.add_object(weapon1)
                            self.game.add_object(weapon2)
                            self.game.add_object(weapon3)
                        else:
                            weapon = Objects.WeaponClass(x=x, y=self.game.objects_dict['player'].y,
                                                         vy=-700, game=self.game)
                            self.game.add_object(weapon)
