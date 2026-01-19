from Modules.Module import *
import raylib

class Movement(Module):
    def __init__(self):
        self.inited = False

    def update(self):
        if not self.inited:
            if not self.parent.get_module('Sprite2D'):
                raise Exception(f'PyLyEngineError: Module "{self.__class__.__name__}" requires "Sprite2D" module')
            if not hasattr(self.parent, 'speed'):
                self.parent.speed = 1
            self.inited = True

        speed = self.parent.speed


        if raylib.IsKeyDown(raylib.KEY_W):
            self.parent.y -= self.parent.speed

        if raylib.IsKeyDown(raylib.KEY_A):
            self.parent.x -= self.parent.speed


        if raylib.IsKeyDown(raylib.KEY_S):
            self.parent.y += self.parent.speed


        if raylib.IsKeyDown(raylib.KEY_D):
            self.parent.x += self.parent.speed



