import pygame
from Objects.Object import ObjectClass


# self.x положение на экране в данный момент времени
# параметр x в конструкторе (__init__)
# это начальное положение на экране в начальный момент времени


class EnemyClass(ObjectClass):
    def __init__(self, x, y, vy, game):
        self.x = x
        self.y = y
        self.vy = vy
        super().__init__(game)

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 200, 200), (self.x, self.y, 10, 10))

    def update(self):
        self.y += self.vy


# class A:
#     # self.x положение на экране в данный момент времени
#     # x_in это начальное положение на экране в начальный момент времени
#     def __init__(self, x_in, y_in):
#         self.x = x_in
#         self.y = y_in
#
#     def update(self):
#         self.x += 1
#         self.y += 1
#
#
# a = A(10, 20)
# # 20 120
# print(a.x, a.y)
# a.update()
# print(a.x, a.y)
# a.update()
# print(a.x, a.y)
