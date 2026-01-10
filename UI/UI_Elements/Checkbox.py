import raylib

class Checkbox:
    def __init__(self, ui_layer, rel_x, rel_y, rel_size, text, initial_checked=False, on_change_func=None, on_change_args=None):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_size = rel_size
        self.text = text.encode()
        self.checked = initial_checked
        self.on_change_action = on_change_func
        self.on_change_args = on_change_args if on_change_args is not None else []

        self.x = 0
        self.y = 0
        self.size = 0
        self.text_size = 0
        self.rel_text_size = 0.4
        self.text_spacing = 0.2
        self.render_mode = 'default'
        self.update_position()

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.size = int(window.width * self.rel_size)
        max_text_size = self.ui_layer.ui_theme['Checkbox'][self.render_mode]['max_text_size']
        min_text_size = self.ui_layer.ui_theme['Checkbox'][self.render_mode]['min_text_size']
        self.text_size = int(self.size * self.rel_text_size)
        self.text_size = max(min_text_size, min(max_text_size, self.text_size))

    def toggle(self):
        self.checked = not self.checked
        if self.on_change_action:
            if self.on_change_args:
                self.on_change_action(self.checked, *self.on_change_args)
            else:
                self.on_change_action(self.checked)

    def update(self):
        self.update_position()
        window = self.ui_layer.parent_scene.window

        text_width = raylib.MeasureText(self.text, self.text_size)
        click_area_width = self.size + int(self.size * self.text_spacing) + text_width
        click_area_height = max(self.size, self.text_size)
        click_area_y = self.y - (click_area_height - self.size) // 2

        self.render_mode = 'default'
        if (window.mouse_x >= self.x and
            window.mouse_x <= self.x + click_area_width and
            window.mouse_y >= click_area_y and
            window.mouse_y <= click_area_y + click_area_height):

            self.render_mode = 'hover'
            if raylib.IsMouseButtonDown(0):
                self.render_mode = 'press'
            if raylib.IsMouseButtonReleased(0):
                self.toggle()

        raylib.DrawRectangleRounded(
            [self.x, self.y, self.size, self.size],
            self.ui_layer.ui_theme['Checkbox']['roundness'],
            self.ui_layer.ui_theme['Checkbox']['segments'],
            self.ui_layer.ui_theme['Checkbox'][self.render_mode]['box_color']
        )

        raylib.DrawRectangleRoundedLinesEx(
            [self.x, self.y, self.size, self.size],
            self.ui_layer.ui_theme['Checkbox']['roundness'],
            self.ui_layer.ui_theme['Checkbox']['segments'],
            self.ui_layer.ui_theme['Checkbox'][self.render_mode]['outline_width'],
            self.ui_layer.ui_theme['Checkbox'][self.render_mode]['outline_color']
        )

        if self.checked:
            check_color = self.ui_layer.ui_theme['Checkbox'][self.render_mode]['check_color']
            padding = int(self.size * 0.2)
            start_x = self.x + padding
            start_y = self.y + self.size // 2
            middle_x = self.x + self.size // 3
            middle_y = self.y + self.size - padding
            end_x = self.x + self.size - padding
            end_y = self.y + padding

            raylib.DrawLineEx(
                [start_x, start_y],
                [middle_x, middle_y],
                self.ui_layer.ui_theme['Checkbox'][self.render_mode]['check_width'],
                check_color
            )
            raylib.DrawLineEx(
                [middle_x, middle_y],
                [end_x, end_y],
                self.ui_layer.ui_theme['Checkbox'][self.render_mode]['check_width'],
                check_color
            )
        text_x = self.x + self.size + int(self.size * self.text_spacing)
        text_y = self.y + (self.size - self.text_size) // 2

        raylib.DrawText(
            self.text,
            text_x,
            text_y,
            self.text_size,
            self.ui_layer.ui_theme['Checkbox'][self.render_mode]['text_color']
        )
