from Game import GameClass

game = GameClass()
# запустил конструктор
game.start()

# Game
# - Object
# - - update
# - - draw
# - Enemies ( Object )
# - Arrow ( Object )
# - - (update_for_arrow())
# - Player ( Object )
# - - handle_events

# class A:
#     def print(self):
#         print('Hello A')
#
#     def print_A(self):
#         print('A')
#
#
# class B(A):
#     x = 10
#     def print(self):
#         print('Hello B')
#
#
# a = A()
# a.print()
# a.print_A()
# b = B()
# b.print()
# b.print_A()
