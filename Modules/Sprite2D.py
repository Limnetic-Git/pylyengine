import raylib
import Extentions.raylib_extention as raylib_ex
from Modules.Module import *
from Animation.Animation import *

class Sprite2D(Module):
    _defaults = {
        'x': 0, 'y': 0, 'scale_x': 1.0, 'scale_y': 1.0,
        'origin': None, 'tint': raylib.WHITE, 'angle': 0,
        'flip_x': False, 'flip_y': False, 'visible': True
    }

    def __init__(self, animation_name, layer=0):
        self.animation_name = animation_name
        self.animation = None
        self.layer_id = layer
        self._texture_name_cache = None

    def set_parent(self, parent):
        super().set_parent(parent)
        for attr, val in self._defaults.items():
            if not hasattr(self.parent, attr):
                setattr(self.parent, attr, val)

    def update(self):
        if not self.parent.visible:
            return

        if self.animation_name != self._texture_name_cache:
            self._texture_name_cache = self.animation_name
            self.animation = Animation(
                frames=self.parent.parent_scene.window.source_manager[self.animation_name],
                source_manager=self.parent.parent_scene.window.source_manager,
                frame_delay=8,
            )
        frame = self.animation.get_current_frame()

        raylib_ex.DrawTexture(
            texture=frame,
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
