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
        if not self.parent.visible: return

        screen_width = self.parent.parent_scene.window.width
        screen_height = self.parent.parent_scene.window.height

        camera = self.parent.parent_scene.camera

        texture = self.window.source_manager[self.get_current_frame()]
        texture_width = texture.width * abs(self.parent.scale_x) * camera.zoom_x
        texture_height = texture.height * abs(self.parent.scale_y) * camera.zoom_y

        world_x = self.parent.x * camera.zoom_x + camera.x
        world_y = self.parent.y * camera.zoom_y + camera.y

        if self.parent.origin:
            origin_x = self.parent.origin[0] * self.parent.scale_x * camera.zoom_x
            origin_y = self.parent.origin[1] * self.parent.scale_y * camera.zoom_y
        else:
            origin_x = texture_width / 2
            origin_y = texture_height / 2

        obj_left = world_x - origin_x
        obj_top = world_y - origin_y
        obj_right = obj_left + texture_width
        obj_bottom = obj_top + texture_height

        screen_left = 0
        screen_top = 0
        screen_right = screen_width
        screen_bottom = screen_height

        if (obj_right < screen_left or
            obj_left > screen_right or
            obj_bottom < screen_top or
            obj_top > screen_bottom):
            return

        raylib_ex.DrawTexture(
            texture=texture,
            position=(world_x, world_y),
            rotation=self.parent.angle,
            scale=(self.parent.scale_x * camera.zoom_x,
                self.parent.scale_y * camera.zoom_y),
            origin=self.parent.origin,
            tint=self.parent.tint,
            flip_x=self.parent.flip_x,
            flip_y=self.parent.flip_y,
        )
