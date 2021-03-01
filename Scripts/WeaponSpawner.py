from Scripts.Script import ScriptClass
from Objects.Weapon import WeaponClass


class WeaponSpawnerClass(ScriptClass):
    def run(self):
        weapon = WeaponClass(self.game.player.x, self.game.player.y, -30, self.game)
        self.game.objects.append(weapon)
