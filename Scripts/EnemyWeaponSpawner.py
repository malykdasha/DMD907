import Scripts
import Objects


class EnemyWeaponSpawner(Scripts.ScriptClass):
    def __init__(self, enemy, game):
        super().__init__(game)
        self.enemy = enemy
        self.time = 0

    def run(self):
        self.time += 1

        if self.time % 20 == 0 and self.enemy.y > 0:
            enemy_weapon_bullet = Objects.EnemyWeapon(x=self.enemy.x, y=self.enemy.y, vy=400, game=self.game)
            self.game.add_object(enemy_weapon_bullet)
