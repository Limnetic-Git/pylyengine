from Objects.Object import *
import raylib
from Animation.Animation import *

class TestObject(Object):
    def __init__(self):
        super().__init__()
        self.scale_x = 1.75
        self.scale_y = 1.75

    def update(self):
        super().update()
        if raylib.IsKeyPressed(raylib.KEY_F):
            self.get_module('SoundEmitter').play()





