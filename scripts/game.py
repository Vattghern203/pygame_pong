from scripts.obj import Obj
from scripts.scene import Scene

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.bg = Obj("assets/china.png", [self.all_sprites])