import Scripts
import Objects


class CheckTouchHelper(Scripts.ScriptClass):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        for helper in self.game.objects:
            if type(helper) is Objects.HelperClass:
                if self.game.objects_dict['player'].x + helper.width\
                        <= helper.x <= self.game.objects_dict['player'].x + self.game.objects_dict['player'].width:
                    if self.game.objects_dict['player'].y - helper.height <= helper.y \
                            <= self.game.objects_dict['player'].y + self.game.objects_dict['player'].height:
                        self.game.objects_dict['health'].add()
                        self.game.objects.remove(helper)
