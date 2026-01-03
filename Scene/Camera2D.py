import raylib

class Camera2D:
    def __init__(self, window):
        self.window = window
        self.x = 0
        self.y = 0
        self.zoom_x = 1.0
        self.zoom_y = 1.0
        self.zoom_step = 0.05

    def set_focus_object(self, object):
        if not object.get_module('Sprite2D'):
            raise Exception('PyLyEngineError: To focus camera on object, requires "Sprite2D" module')
            return

        self.focus_object = object

    def update(self):
        if hasattr(self, 'focus_object'):
            self.x = self.window.width // 2 - self.focus_object.x * self.zoom_x
            self.y = self.window.height // 2 - self.focus_object.y * self.zoom_y
        wheel_move = raylib.GetMouseWheelMove()
        if wheel_move != 0:
            self.zoom_x += self.zoom_step * wheel_move
            self.zoom_y += self.zoom_step * wheel_move



