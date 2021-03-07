from Scripts.Script import ScriptClass
from Objects.Weapon import WeaponClass


class WeaponSpawnerClass(ScriptClass):
    def run(self):
        weapon = WeaponClass(self.game.current_level.player.x, self.game.current_level.player.y, -30, self.game)
        self.game.current_level.objects.append(weapon)
