from Objects.Object import *
import raylib
from Animation.Animation import *

class Player(Object):
    def __init__(self):
        self.name = 'player'
        self.speed = 2

        self.scale_x = 1.75
        self.scale_y = 1.75

        super().__init__()

        
    def update(self):
        if raylib.IsKeyDown(raylib.KEY_A):
            self.flip_x = True

        if raylib.IsKeyDown(raylib.KEY_D):
            self.flip_x = False



        super().update()



