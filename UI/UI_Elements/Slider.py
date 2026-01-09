import raylib

class Slider:
    def __init__(self, ui_layer, rel_x, rel_y, rel_width, rel_height, min_value, max_value, initial_value, on_change_func, on_change_args):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.on_change_action = on_change_func
        self.on_change_args = on_change_args if on_change_args is not None else []
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.slider_handle_x = 0
        self.slider_handle_width = 0
        self.slider_handle_height = 0
        self.is_dragging = False
        self.render_mode = 'default'

        self.update_position()

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)
        self.slider_handle_width = int(self.height * 1.5)
        self.slider_handle_height = int(self.height * 2)
        self.update_slider_position()

    def update_slider_position(self):
        value_range = self.max_value - self.min_value
        if value_range == 0:
            self.slider_handle_x = self.x
        else:
            normalized_value = (self.value - self.min_value) / value_range
            self.slider_handle_x = self.x + int(normalized_value * (self.width - self.slider_handle_width))

    def set_value(self, value):
        self.value = max(self.min_value, min(self.max_value, value))
        self.update_slider_position()

    def update_value_from_position(self, mouse_x):
        clamped_x = max(self.x, min(mouse_x - self.slider_handle_width // 2, self.x + self.width - self.slider_handle_width))

        normalized_pos = (clamped_x - self.x) / (self.width - self.slider_handle_width)
        new_value = self.min_value + normalized_pos * (self.max_value - self.min_value)

        if isinstance(self.min_value, int) and isinstance(self.max_value, int):
            new_value = round(new_value)

        if new_value != self.value:
            self.value = new_value
            self.slider_handle_x = clamped_x
            if self.on_change_args:
                self.on_change_action(self.value, *self.on_change_args)
            else:
                self.on_change_action(self.value)

    def on_click(self, mouse_x, mouse_y):
        if (mouse_x >= self.x and mouse_x <= self.x + self.width and
            mouse_y >= self.y - self.slider_handle_height // 4 and
            mouse_y <= self.y + self.height + self.slider_handle_height // 4):
            if (mouse_x >= self.slider_handle_x and
                mouse_x <= self.slider_handle_x + self.slider_handle_width and
                mouse_y >= self.y - self.slider_handle_height // 4 + self.height // 2 and
                mouse_y <= self.y + self.slider_handle_height // 4 + self.height // 2):
                self.is_dragging = True
            else:
                self.update_value_from_position(mouse_x)

    def update(self):
        self.update_position()
        window = self.ui_layer.parent_scene.window
        mouse_in_slider = (window.mouse_x >= self.x and
                          window.mouse_x <= self.x + self.width and
                          window.mouse_y >= self.y - self.slider_handle_height // 4 and
                          window.mouse_y <= self.y + self.height + self.slider_handle_height // 4)

        mouse_in_handle = (window.mouse_x >= self.slider_handle_x and
                          window.mouse_x <= self.slider_handle_x + self.slider_handle_width and
                          window.mouse_y >= self.y - self.slider_handle_height // 4 + self.height // 2 and
                          window.mouse_y <= self.y + self.slider_handle_height // 4 + self.height // 2)
        if raylib.IsMouseButtonPressed(0) and (mouse_in_slider or mouse_in_handle):
            self.is_dragging = True
        if self.is_dragging:
            if raylib.IsMouseButtonDown(0):
                self.update_value_from_position(window.mouse_x)
            else:
                self.is_dragging = False
        self.render_mode = 'default'
        if mouse_in_slider or self.is_dragging:
            self.render_mode = 'hover'
            if mouse_in_handle or self.is_dragging:
                if raylib.IsMouseButtonDown(0):
                    self.render_mode = 'press'
        track_rect = [
            self.x,
            self.y + self.height // 2 - self.ui_layer.ui_theme['Slider']['track_height'] // 2,
            self.width,
            self.ui_layer.ui_theme['Slider']['track_height']
        ]

        raylib.DrawRectangleRounded(
            track_rect,
            self.ui_layer.ui_theme['Slider']['track_roundness'],
            self.ui_layer.ui_theme['Slider']['segments'],
            self.ui_layer.ui_theme['Slider'][self.render_mode]['track_color']
        )
        if self.value > self.min_value:
            filled_width = self.slider_handle_x + self.slider_handle_width // 2 - self.x
            if filled_width > 0:
                filled_rect = [
                    self.x,
                    self.y + self.height // 2 - self.ui_layer.ui_theme['Slider']['track_height'] // 2,
                    filled_width,
                    self.ui_layer.ui_theme['Slider']['track_height']
                ]

                raylib.DrawRectangleRounded(
                    filled_rect,
                    self.ui_layer.ui_theme['Slider']['track_roundness'],
                    self.ui_layer.ui_theme['Slider']['segments'],
                    self.ui_layer.ui_theme['Slider'][self.render_mode]['filled_color']
                )
        handle_rect = [
            self.slider_handle_x,
            self.y + self.height // 2 - self.slider_handle_height // 2,
            self.slider_handle_width,
            self.slider_handle_height
        ]

        raylib.DrawRectangleRounded(
            handle_rect,
            self.ui_layer.ui_theme['Slider']['handle_roundness'],
            self.ui_layer.ui_theme['Slider']['segments'],
            self.ui_layer.ui_theme['Slider'][self.render_mode]['handle_color']
        )

        raylib.DrawRectangleRoundedLinesEx(
            handle_rect,
            self.ui_layer.ui_theme['Slider']['handle_roundness'],
            self.ui_layer.ui_theme['Slider']['segments'],
            self.ui_layer.ui_theme['Slider'][self.render_mode]['handle_outline_width'],
            self.ui_layer.ui_theme['Slider'][self.render_mode]['handle_outline_color']
        )
        if self.ui_layer.ui_theme['Slider']['show_value']:
            value_text = f"{self.value:.1f}" if isinstance(self.value, float) else f"{self.value}"
            text_size = self.ui_layer.ui_theme['Slider']['value_text_size']
            text_width = raylib.MeasureText(value_text.encode(), text_size)
            if self.ui_layer.ui_theme['Slider']['value_position'] == 'above':
                text_y = self.y - text_size - 5
            else:
                text_y = self.y + self.height + 5
            text_x = self.slider_handle_x + self.slider_handle_width // 2 - text_width // 2
            raylib.DrawText(
                value_text.encode(),
                text_x,
                text_y,
                text_size,
                self.ui_layer.ui_theme['Slider'][self.render_mode]['value_text_color']
            )
