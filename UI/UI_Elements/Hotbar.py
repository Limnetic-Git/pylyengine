from UI.UI_Elements.Texture import *
from UI.UI_Elements.Text import *
import raylib


class Hotbar:
    def __init__(self, ui_layer, inventory, rel_x, rel_y, slot_size, slotline_index, distance_between=5):
        self.inventory = inventory
        self.array = self.inventory.inventory
        self.slotline_index = 0
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = slot_size / 1920
        self.rel_height = slot_size / 1080
        self.distance_between = distance_between
        self.item_buffer = {'item': None, 'count': 0, 'parent_slot': [-1, -1]}
        self.selected_slot = 0

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)

    def update(self):
        window = self.ui_layer.parent_scene.window
        self.update_position()

        for x in range(len(self.array)):
            y = self.slotline_index
            render_mode = 'default'
            slot_x = self.x + x * (self.width + self.distance_between)
            slot_y = self.y + y * (self.height + self.distance_between)

            mouse_over = (window.mouse_x >= slot_x and window.mouse_x <= slot_x + self.width and
                            window.mouse_y >= slot_y and window.mouse_y <= slot_y + self.height)

            if mouse_over:
                render_mode = "hover"

            if x == self.selected_slot:
                render_mode = "selected"

            raylib.DrawRectangleRounded(
                [slot_x, slot_y, self.width, self.height],
                self.ui_layer.ui_theme['Slotlist']['roundness'],
                self.ui_layer.ui_theme['Slotlist']['segments'],
                self.ui_layer.ui_theme['Slotlist'][render_mode]['main_color'],
            )

            raylib.DrawRectangleRoundedLinesEx(
                [slot_x, slot_y, self.width, self.height],
                self.ui_layer.ui_theme['Slotlist']['roundness'],
                self.ui_layer.ui_theme['Slotlist']['segments'],
                self.ui_layer.ui_theme['Slotlist'][render_mode]['outline_width'],
                self.ui_layer.ui_theme['Slotlist'][render_mode]['outline_color'],
            )

            slot_item = self.array[x][y]
            if slot_item['item'] and slot_item['count'] > 0:
                items_in_slot = slot_item['count']

                if (self.item_buffer['parent_slot'] == [x, y] and
                    self.item_buffer['item'] == slot_item['item']):
                    items_in_slot -= self.item_buffer['count']

                if items_in_slot > 0:
                    texture_element_x = slot_x / window.width + (3 / 1920)
                    texture_element_y = slot_y / window.height + (3 / 1080)
                    texture_element_width = self.rel_width - (6 / 1920)
                    texture_element_height = self.rel_height - (6 / 1080)

                    texture_element = Texture(
                        self.ui_layer,
                        texture_element_x,
                        texture_element_y,
                        texture_element_width,
                        texture_element_height,
                        slot_item['item'].texture_name,
                        raylib.WHITE,
                    )

                    text_element = Text(
                        self.ui_layer,
                        texture_element_x - texture_element_width + 0.015,
                        texture_element_y + 0.01,
                        0.075,
                        0.075,
                        str(items_in_slot),
                        raylib.RAYWHITE,
                    )
                    texture_element.update()
                    text_element.update()

        wheel_move = raylib.GetMouseWheelMove()
        if wheel_move and not raylib.IsKeyDown(raylib.KEY_LEFT_CONTROL):
            if wheel_move < 0:
                self.selected_slot -= 1
                if self.selected_slot < 0:
                    self.selected_slot = len(self.array) - 1
            else:
                self.selected_slot += 1
                if self.selected_slot >= len(self.array):
                    self.selected_slot = 0


