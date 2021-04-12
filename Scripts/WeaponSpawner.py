import Objects
import Scripts


class WeaponSpawnerClass(Scripts.ScriptClass):
    def run(self):
        weapon = Objects.WeaponClass(x=self.game.current_level.player.x + self.game.current_level.player.width/2,
                                     y=self.game.current_level.player.y,
                                     vy=-30,
                                     game=self.game)
        self.game.current_level.weapon.append(weapon)
        self.game.current_level.objects.append(weapon)
