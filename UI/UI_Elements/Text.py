import raylib

class Text:
    def __init__(self, ui_layer, rel_x, rel_y, rel_width, rel_height, text):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height
        self.text = text.encode()
        self.rel_text_size = 0.4
        self.min_text_size = 36
        self.max_text_size = 56
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.text_size = 36
        self.render_mode = 'default'
        self.update_position()

    def update_position(self):
        window = self.ui_layer.parent_scene.window

        self.max_text_size = self.ui_layer.ui_theme['Text'][self.render_mode]['max_text_size']
        self.min_text_size = self.ui_layer.ui_theme['Text'][self.render_mode]['min_text_size']
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)
        self.text_size = int(self.height * self.rel_text_size)
        self.text_size = max(self.min_text_size,
                         min(self.max_text_size, self.text_size))


    def update(self):
        self.update_position()
        window = self.ui_layer.parent_scene.window
        self.render_mode = 'default'
        text_width = raylib.MeasureText(self.text, self.text_size)
        text_x = self.x + (self.width - text_width) // 2
        text_y = self.y + (self.height - self.text_size) // 2
        raylib.DrawText(self.text, text_x, text_y, self.text_size, self.ui_layer.ui_theme['Text'][self.render_mode]['text_color'])
