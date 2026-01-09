import raylib

class Area:
    def __init__(self, ui_layer, rel_x, rel_y, rel_width, rel_height):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.render_mode = 'default'
        self.update_position()

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)


    def update(self):
        self.update_position()
        window = self.ui_layer.parent_scene.window

        self.render_mode = 'default'

        raylib.DrawRectangleRounded(
            [self.x, self.y, self.width, self.height],
            self.ui_layer.ui_theme['Area']['roundness'],
            self.ui_layer.ui_theme['Area']['segments'],
            self.ui_layer.ui_theme['Area'][self.render_mode]['main_color']
        )
        raylib.DrawRectangleRoundedLinesEx(
            [self.x, self.y, self.width, self.height],
            self.ui_layer.ui_theme['Area']['roundness'],
            self.ui_layer.ui_theme['Area']['segments'],
            self.ui_layer.ui_theme['Area'][self.render_mode]['outline_width'],
            self.ui_layer.ui_theme['Area'][self.render_mode]['outline_color'],
        )
