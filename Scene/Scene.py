import raylib
from Scene.Camera2D import *

class Scene:
    def __init__(self, window):
        self.camera = Camera2D(window)
        self.window = window
        self.objects = []
        self._needs_layer_sort = False

    def add_object(self, object):
        sprite_module = object.get_module('Sprite2D')
        if sprite_module:
            sprite_module.set_window(self.window)
        object.set_parent_scene(self)
        self.objects.append(object)
        self._needs_layer_sort = True

    def get_object_by_name(self, name):
        for object in self.objects:
            if hasattr(object, 'name'):
                if object.name == name:
                    return object

    def __get_layer_id(self, object):
        sprite_module = object.get_module('Sprite2D')
        if hasattr(object, 'layer_id'):
            return object.layer_id
        if sprite_module:
            return sprite_module.layer_id
        return 0

    def sort_objects_by_layer(self):
        self.objects = sorted(self.objects, key=self.__get_layer_id)
        self._needs_layer_sort = False

    def update(self):
        self.window.width = raylib.GetScreenWidth()
        self.window.height = raylib.GetScreenHeight()

        raylib.BeginDrawing()
        raylib.ClearBackground(raylib.WHITE)
        if self._needs_layer_sort:
            self.sort_objects_by_layer()
        self.camera.update()
        for object in self.objects:
            object.update()
        self.window.debug_monitor.update()

        raylib.EndDrawing()

