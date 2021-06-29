import Scripts
import Objects


class CheckTouchEnemy(Scripts.ScriptClass):
    def __init__(self, enemy, game):
        super().__init__(game)
        self.enemy = enemy

    def run(self):
        for player_weapon in self.game.objects:
            if type(player_weapon) is Objects.WeaponClass:
                if player_weapon.x - self.enemy.width <= self.enemy.x <= player_weapon.x + player_weapon.width:
                    if player_weapon.y - self.enemy.height <= self.enemy.y <= player_weapon.y + player_weapon.height:
                        if self.enemy.health > 1:
                            self.enemy.health -= 1
                        else:
                            self.game.objects.remove(self.enemy)
                        self.game.objects.remove(player_weapon)
