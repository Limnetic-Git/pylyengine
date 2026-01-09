import raylib

class Button:
    def __init__(self, ui_layer, rel_x, rel_y, rel_width, rel_height, text, func, args):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height
        self.text = text.encode()
        self.rel_text_size = 0.4
        self.min_text_size = 12
        self.max_text_size = 36
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.text_size = 20
        self.update_position()

        self.on_click_action = func
        self.on_click_args = args

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)
        self.text_size = int(self.height * self.rel_text_size)
        self.text_size = max(self.min_text_size,
                           min(self.max_text_size, self.text_size))
    def on_click(self):
        self.on_click_action(*self.on_click_args)

    def update(self):
        self.update_position()
        window = self.ui_layer.parent_scene.window

        render_mode = 'default'
        if window.mouse_x >= self.x and window.mouse_x <= self.x + self.width and \
           window.mouse_y >= self.y and window.mouse_y <= self.y + self.height:
               render_mode = 'hover'
               if raylib.IsMouseButtonDown(0):
                   render_mode = 'press'
               if raylib.IsMouseButtonReleased(0):
                   self.on_click()

        raylib.DrawRectangleRounded(
            [self.x, self.y, self.width, self.height],
            self.ui_layer.ui_theme['Button']['roundness'],
            self.ui_layer.ui_theme['Button']['segments'],
            self.ui_layer.ui_theme['Button'][render_mode]['main_color']
        )
        raylib.DrawRectangleRoundedLinesEx(
            [self.x, self.y, self.width, self.height],
            self.ui_layer.ui_theme['Button']['roundness'],
            self.ui_layer.ui_theme['Button']['segments'],
            self.ui_layer.ui_theme['Button'][render_mode]['outline_width'],
            self.ui_layer.ui_theme['Button'][render_mode]['outline_color'],
        )

        text_width = raylib.MeasureText(self.text, self.text_size)
        text_x = self.x + (self.width - text_width) // 2
        text_y = self.y + (self.height - self.text_size) // 2
        raylib.DrawText(self.text, text_x, text_y, self.text_size, self.ui_layer.ui_theme['Button'][render_mode]['text_color'])
