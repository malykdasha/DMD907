import pygame

from Objects.Object import ObjectClass


class ButtonClass(ObjectClass):
    def __init__(self, x, y, width, height, text, function, game):
        super().__init__(game)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.function = function

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (255, 0, 200),
                         (self.x, self.y, self.width, self.height))

    def update(self):
        mouse = pygame.mouse.get_pos()
        # mouse[0] -> x
        # mouse[1] -> y
        click = pygame.mouse.get_pressed(3)
        # click[0] -> left button on mouse
        # == 1 -> pressed
        if click[0] == 1 and \
                self.x < mouse[0] < self.x + self.width and \
                self.y < mouse[1] < self.y + self.height:
            self.function(self)
    #         action()
    # def is_pressed(self, action):
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()
    #     if click[0] == 1 and self.x < mouse[0] < self.x+self.w and self.y < mouse[1] < self.y + self.h:
    #         action()



