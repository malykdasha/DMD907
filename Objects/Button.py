import pygame

from Objects.Object import ObjectClass


class ButtonClass(ObjectClass):
    def __init__(self,x,y,w,h,text,game):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        super().__init__(game)

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 200), (self.x, self.y, self.w, self.h))

    def is_pressed(self, action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and self.x < mouse[0] < self.x+self.w and self.y < mouse[1] < self.y + self.h:
            action()



