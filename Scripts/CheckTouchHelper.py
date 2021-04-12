import Scripts
import Objects


class CheckTouchHelper(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        for helper in self.game.objects:
            if type(helper) is Objects.HelperClass:
                if self.game.objects_dict['player'].x - 10 <= helper.x <= self.game.objects_dict['player'].x + 40:
                    if self.game.HEIGHT - 50 <= helper.y <= self.game.HEIGHT - 40:
                        self.game.objects_dict['health'].add()
                        self.game.objects.remove(helper)