import raylib
import random

class Camera2D:
    def __init__(self, scene):
        self.window = scene.window
        self.x = 0
        self.y = 0
        self.zoom_x = 1.0
        self.zoom_y = 1.0
        self.zoom_step = 0.05

        self.mouse_x = 0
        self.mouse_y = 0

        self.shake = False
        self.shake_power_x = 5
        self.shake_power_y = 3
        self.shake_delay = 5
        self.shake_tick = 0
        self.shake_offset_x = 0
        self.shake_offset_y = 0

    def set_focus_object(self, object):
        if not object.get_module('Sprite2D'):
            raise Exception('PyLyEngineError: To focus camera on object, requires "Sprite2D" module')
        self.focus_object = object

    def update(self):
        self.shake_tick += 1
        self.mouse_x = int((self.window.mouse_x - self.x) / self.zoom_x)
        self.mouse_y = int((self.window.mouse_y - self.y) / self.zoom_y)

        wheel_move = raylib.GetMouseWheelMove()
        if raylib.IsKeyDown(raylib.KEY_LEFT_CONTROL):
            if wheel_move != 0:
                self.zoom_x += self.zoom_step * wheel_move
                self.zoom_y += self.zoom_step * wheel_move
        if hasattr(self, 'focus_object'):
            self.x = int(self.window.width // 2 - self.focus_object.x * self.zoom_x)
            self.y = int(self.window.height // 2 - self.focus_object.y * self.zoom_y)
        if self.shake:
            if self.shake_tick % self.shake_delay == 0:
                self.shake_offset_x = self.shake_power_x * random.choice([1, 0, -1])
                self.shake_offset_y = self.shake_power_y * random.choice([1, 0, -1])
            self.x += self.shake_offset_x
            self.y += self.shake_offset_y
        else:

            self.shake_offset_x = 0
            self.shake_offset_y = 0
