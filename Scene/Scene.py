import raylib
from Scene.Camera2D import *

class Scene:
    def __init__(self, window):
        self.camera = Camera2D(window)
        self.window = window
        self.objects = []

    def add_object(self, object):
        sprite_module = object.get_module('Sprite2D')
        if sprite_module:
            sprite_module.set_window(self.window)
        object.set_parent_scene(self)
        self.objects.append(object)

    def get_object_by_name(self, name):
        for object in self.objects:
            if hasattr(object, 'name'):
                if object.name == name:
                    return object

    def get_layer_id(self, object):
        sprite_module = object.get_module('Sprite2D')
        if sprite_module:
            return sprite_module.layer_id
        return 0

    def sort_objects_by_layer(self):
        self.objects = sorted(self.objects, key=self.get_layer_id)

    def update(self):
        raylib.BeginDrawing()
        raylib.ClearBackground(raylib.WHITE)

        self.sort_objects_by_layer()
        for object in self.objects:
            object.update()
        self.camera.update()

        raylib.EndDrawing()

