class ObjectClass:
    def __init__(self, game):
        self.game = game
        self.scripts = []

    def update(self):
        pass

    def draw(self):
        pass

    def run_scripts(self):
        for script in self.scripts:
            script.run()
