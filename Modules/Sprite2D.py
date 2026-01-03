import raylib
import Extentions.raylib_extention as raylib_ex
from Modules.Module import *


class Sprite2D(Module):
    def __init__(self, frames, frame_delay=1, layer_id=0):
        self.frames = frames
        self.frame_delay = frame_delay
        self.current_frame_index = 0
        self.animation_tick = 0
        self.layer_id = layer_id

    def set_parent(self, parent):
        super().set_parent(parent)
        _defaults = {
            'x': 0,
            'y': 0,
            'scale_x': 1.0,
            'scale_y': 1.0,
            'origin': None,
            'tint': raylib.WHITE,
            'angle': 0,
            'flip_x': False,
            'flip_y': False,
            'visible': True
        }

        for attr, default_value in _defaults.items():
            if not hasattr(self.parent, attr):
                setattr(self.parent, attr, default_value)

    def get_current_frame(self):
        if len(self.frames) > 1:
            self.animation_tick += 1
            if self.animation_tick % self.frame_delay == 0:
                self.animation_tick = 0
                if self.current_frame_index == len(self.frames) - 1:
                    self.current_frame_index = 0
                else:
                    self.current_frame_index += 1
            return self.frames[self.current_frame_index]
        else:
            return self.frames[0]

    def update(self):
        if self.parent.visible:
            raylib_ex.DrawTexture(
                texture=self.window.source_manager[self.get_current_frame()],
                position=(self.parent.x * self.parent.parent_scene.camera.zoom_x + self.parent.parent_scene.camera.x,
                          self.parent.y * self.parent.parent_scene.camera.zoom_y + self.parent.parent_scene.camera.y),
                rotation=(self.parent.angle),
                scale=(self.parent.scale_x * self.parent.parent_scene.camera.zoom_x,
                       self.parent.scale_y * self.parent.parent_scene.camera.zoom_y),
                origin=self.parent.origin,
                tint=self.parent.tint,
                flip_x=self.parent.flip_x,
                flip_y=self.parent.flip_y,
            )
    
