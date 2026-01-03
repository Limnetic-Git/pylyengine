import raylib

class Camera2D:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom_x = 1.0
        self.zoom_y = 1.0
        self.zoom_step = 0.05

    def set_focus_object(self, object):
        self.focus_object = object

    def update(self):
        if hasattr(self, 'focus_object'):
            self.x = 600 - self.focus_object.x * self.zoom_x
            self.y = 400 - self.focus_object.y * self.zoom_y
        wheel_move = raylib.GetMouseWheelMove()
        if wheel_move != 0:
            self.zoom_x += self.zoom_step * wheel_move
            self.zoom_y += self.zoom_step * wheel_move



