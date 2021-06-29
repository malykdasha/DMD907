import pygame
import Objects


class ButtonClass(Objects.ObjectClass):
    def __init__(self, x, y, width, height, font, text, function, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, font)
        self.function = function
        self.text_ = text
        self.text = self.font.render(text, True, (0, 0, 0))
        self.x_delta = (self.width - self.font.size(self.text_)[0]) / 2
        self.y_delta = (self.height - self.font.size(self.text_)[1]) / 2

        self.color_normal = (255, 0, 200)
        self.color_in = (200, 100, 150)
        self.color = self.color_normal

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         self.color,
                         (self.x, self.y, self.width, self.height))
        self.game.screen.blit(self.text, (self.x + self.x_delta, self.y + self.y_delta))

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if self.x < mouse[0] < self.x + self.width and \
                self.y < mouse[1] < self.y + self.height:
            if click[0] == 1:
                self.function(self)
            else:
                self.color = self.color_in
        else:
            self.color = self.color_normal
