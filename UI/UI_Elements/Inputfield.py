import raylib
import time

class InputField:
    def __init__(self, ui_layer, rel_x, rel_y, rel_width, rel_height, initial_text="",
                 max_length=100, on_enter_func=None, on_enter_args=None):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height
        self.text = initial_text.encode()
        self.max_length = max_length
        self.on_enter_action = on_enter_func
        self.on_enter_args = on_enter_args if on_enter_args is not None else []

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.text_size = 0
        self.rel_text_size = 0.6
        self.render_mode = 'default'
        self.is_focused = False
        self.cursor_position = len(initial_text)
        self.cursor_visible = True
        self.cursor_blink_time = 0.5  # секунды
        self.last_blink_time = time.time()
        self.update_position()

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)

        max_text_size = self.ui_layer.ui_theme['InputField'][self.render_mode]['max_text_size']
        min_text_size = self.ui_layer.ui_theme['InputField'][self.render_mode]['min_text_size']
        self.text_size = int(self.height * self.rel_text_size)
        self.text_size = max(min_text_size, min(max_text_size, self.text_size))

    def set_focus(self, focused):
        self.is_focused = focused
        if focused:
            self.cursor_position = len(self.text)
            self.cursor_visible = True
            self.last_blink_time = time.time()

    def insert_text(self, text):
        if len(self.text) + len(text) <= self.max_length:
            text_bytes = self.text
            self.text = text_bytes[:self.cursor_position] + text.encode() + text_bytes[self.cursor_position:]
            self.cursor_position += len(text)

    def delete_backward(self):
        if self.cursor_position > 0:
            text_bytes = self.text
            self.text = text_bytes[:self.cursor_position-1] + text_bytes[self.cursor_position:]
            self.cursor_position -= 1

    def delete_forward(self):
        if self.cursor_position < len(self.text):
            text_bytes = self.text
            self.text = text_bytes[:self.cursor_position] + text_bytes[self.cursor_position+1:]

    def move_cursor_left(self):
        if self.cursor_position > 0:
            self.cursor_position -= 1

    def move_cursor_right(self):
        if self.cursor_position < len(self.text):
            self.cursor_position += 1

    def handle_key_input(self):
        key = raylib.GetCharPressed()
        while key > 0:
            if (key >= 32 and key <= 125) or (key >= 192 and key <= 255):
                self.insert_text(chr(key))
            key = raylib.GetCharPressed()
        if raylib.IsKeyPressed(raylib.KEY_BACKSPACE):
            self.delete_backward()
        elif raylib.IsKeyPressed(raylib.KEY_DELETE):
            self.delete_forward()
        elif raylib.IsKeyPressed(raylib.KEY_LEFT):
            self.move_cursor_left()
        elif raylib.IsKeyPressed(raylib.KEY_RIGHT):
            self.move_cursor_right()
        elif raylib.IsKeyPressed(raylib.KEY_ENTER) or raylib.IsKeyPressed(raylib.KEY_KP_ENTER):
            if self.on_enter_action:
                if self.on_enter_args:
                    self.on_enter_action(self.text.decode(), *self.on_enter_args)
                else:
                    self.on_enter_action(self.text.decode())

    def update(self):
        self.update_position()
        window = self.ui_layer.parent_scene.window
        mouse_in_field = (window.mouse_x >= self.x and
                         window.mouse_x <= self.x + self.width and
                         window.mouse_y >= self.y and
                         window.mouse_y <= self.y + self.height)

        if raylib.IsMouseButtonPressed(0):
            if mouse_in_field:
                self.set_focus(True)
            else:
                self.set_focus(False)
        if self.is_focused:
            self.render_mode = 'press'
        elif mouse_in_field:
            self.render_mode = 'hover'
        else:
            self.render_mode = 'default'

        if self.is_focused:
            self.handle_key_input()
            current_time = time.time()
            if current_time - self.last_blink_time > self.cursor_blink_time:
                self.cursor_visible = not self.cursor_visible
                self.last_blink_time = current_time

        raylib.DrawRectangleRounded(
            [self.x, self.y, self.width, self.height],
            self.ui_layer.ui_theme['InputField']['roundness'],
            self.ui_layer.ui_theme['InputField']['segments'],
            self.ui_layer.ui_theme['InputField'][self.render_mode]['background_color']
        )
        raylib.DrawRectangleRoundedLinesEx(
            [self.x, self.y, self.width, self.height],
            self.ui_layer.ui_theme['InputField']['roundness'],
            self.ui_layer.ui_theme['InputField']['segments'],
            self.ui_layer.ui_theme['InputField'][self.render_mode]['outline_width'],
            self.ui_layer.ui_theme['InputField'][self.render_mode]['outline_color']
        )
        text = self.text.decode() if self.text else ""
        text_x = self.x + 10
        text_y = self.y + (self.height - self.text_size) // 2
        display_text = text
        text_width = raylib.MeasureText(display_text.encode(), self.text_size)

        if text_width > self.width - 20:
            text_before_cursor = text[:self.cursor_position]
            cursor_pixel_pos = raylib.MeasureText(text_before_cursor.encode(), self.text_size)
            if cursor_pixel_pos > self.width - 30:
                shift_pixels = cursor_pixel_pos - (self.width - 30)
                for i in range(len(text)):
                    if raylib.MeasureText(text[i:].encode(), self.text_size) <= self.width - 20:
                        display_text = text[i:]
                        break
        raylib.DrawText(
            display_text.encode(),
            text_x,
            text_y,
            self.text_size,
            self.ui_layer.ui_theme['InputField'][self.render_mode]['text_color']
        )
        if self.is_focused and self.cursor_visible:
            cursor_in_display = max(0, self.cursor_position - (len(text) - len(display_text)))
            text_before_cursor = display_text[:cursor_in_display]
            cursor_x = text_x + raylib.MeasureText(text_before_cursor.encode(), self.text_size)
            cursor_height = int(self.text_size * 0.8)
            cursor_y = text_y + (self.text_size - cursor_height) // 2
            raylib.DrawRectangle(
                cursor_x,
                cursor_y,
                self.ui_layer.ui_theme['InputField'][self.render_mode]['cursor_width'],
                cursor_height,
                self.ui_layer.ui_theme['InputField'][self.render_mode]['cursor_color']
            )
        if self.ui_layer.ui_theme['InputField']['show_counter']:
            counter_text = f"{len(text)}/{self.max_length}"
            counter_size = int(self.text_size * 0.7)
            counter_width = raylib.MeasureText(counter_text.encode(), counter_size)
            counter_x = self.x + self.width - counter_width - 10
            counter_y = self.y + self.height + 5
            raylib.DrawText(
                counter_text.encode(),
                counter_x,
                counter_y,
                counter_size,
                self.ui_layer.ui_theme['InputField'][self.render_mode]['counter_color']
            )
