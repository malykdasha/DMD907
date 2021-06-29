import pygame
import Scripts
import Objects


class CheckTouchClass(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)
        self.sound_of_touch = pygame.mixer.Sound('Sources/Звук_урона_в_Майнкрафт.wav')

    def run(self):
        for enemy in self.game.objects:
            if type(enemy) is Objects.EnemyClass:
                if self.game.objects_dict['player'].x - enemy.width <= enemy.x \
                        <= self.game.objects_dict['player'].x + self.game.objects_dict['player'].width:
                    if self.game.objects_dict['player'].y - enemy.height <= enemy.y \
                            <= self.game.objects_dict['player'].y + self.game.objects_dict['player'].height:
                        self.game.objects.remove(enemy)
                        self.sound_of_touch.play()
                        if self.game.objects_dict['health'].remove():
                            return True

        for enemy_weapon in self.game.objects:
            if type(enemy_weapon) == Objects.EnemyWeapon:
                if self.game.objects_dict['player'].x - enemy_weapon.width <= enemy_weapon.x \
                        <= self.game.objects_dict['player'].x + self.game.objects_dict['player'].width:
                    if self.game.objects_dict['player'].y - enemy_weapon.height <= enemy_weapon.y \
                            <= self.game.objects_dict['player'].y + self.game.objects_dict['player'].height:
                        self.game.objects.remove(enemy_weapon)
                        self.sound_of_touch.play()
                        if self.game.objects_dict['health'].remove():
                            return True
