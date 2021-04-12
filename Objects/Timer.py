import pygame
import Objects


class TimerClass(Objects.ObjectClass):
    def __init__(self, game):
        super().__init__(game)
        self.start_time = pygame.time.get_ticks()

    def draw(self):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(str((pygame.time.get_ticks() - self.start_time) / 1000), False, (255, 192, 203))
        self.game.screen.blit(text_surface, (self.game.WIDTH / 2, 0))
