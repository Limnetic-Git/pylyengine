import raylib
import Extentions.raylib_extention as raylib_ex
from Modules.Module import *

class Sprite2D(Module):
    _defaults = {
        'x': 0, 'y': 0, 'scale_x': 1.0, 'scale_y': 1.0,
        'origin': None, 'tint': raylib.WHITE, 'angle': 0,
        'flip_x': False, 'flip_y': False, 'visible': True
    }

    def __init__(self, animation, layer=0):
        self.animation = animation
        self.layer_id = layer
        self._texture_cache = None
        self._texture_key = None

    def set_parent(self, parent):
        super().set_parent(parent)
        for attr, val in self._defaults.items():
            if not hasattr(self.parent, attr):
                setattr(self.parent, attr, val)

    def update(self):
        if not self.parent.visible:
            return

        frame = self.animation.get_current_frame()
        if frame != self._texture_key:
            self._texture_key = frame
            self._texture_cache = self.parent.parent_scene.window.source_manager[frame]

        raylib_ex.DrawTexture(
            texture=self._texture_cache,
            position=(self.parent.x, self.parent.y),
            rotation=self.parent.angle,
            scale=(self.parent.scale_x, self.parent.scale_y),
            window=self.parent.parent_scene.window,
            camera=self.parent.parent_scene.camera,
            origin=self.parent.origin,
            tint=self.parent.tint,
            flip_x=self.parent.flip_x,
            flip_y=self.parent.flip_y,
        )
