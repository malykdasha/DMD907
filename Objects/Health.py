import pygame
import Objects
import Levels


class HealthClass(Objects.ObjectClass):
    def __init__(self, game):
        self.x = game.WIDTH / 2
        self.y = game.HEIGHT - 50
        self.radius = 10
        self.value = 10
        super().__init__(game)
        self.img = pygame.image.load('Sources/Images/heart.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.radius * 2, self.radius * 2))

    def add(self):
        if self.value != 10:
            self.value += 1

    def remove(self):
        self.value -= 1
        self.game.shake_ticks += 20
        if self.value == 0:
            timer = self.game.objects_dict['timer']
            time = (pygame.time.get_ticks() - timer.start_time) / 1000
            file = open('score.data', 'w+')
            level_diff = type(self.game.current_level)
            self.game.current_level = Levels.GameOver(self.game, level_diff)
            return True

    def draw(self):
        for i in range(self.value):
            self.game.screen.blit(self.img, ((i + 2) * 25, self.y))
            # pygame.draw.circle(self.game.screen, (0, 0, 0), ((i + 1) * 25, self.y), self.radius)
