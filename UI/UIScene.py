from UI.UI_Elements.Button import *
from UI.UI_Elements.Area import *
from UI.UI_Elements.Text import *
from UI.UI_Elements.Slider import *
from UI.UI_Elements.Checkbox import *
from UI.UI_Elements.Inputfield import *
from UI.UI_Elements.Texture import *
from UI.UI_Elements.Slotlist import *
import ast
import os

class UIScene:
    def __init__(self):
        self.ui_elements = []
        self.ui_theme_name = 'DarkBlueContrast'
        self.ui_theme = {}
        self.__init_ui_themes()

    def set_parent_scene(self, scene):
        self.parent_scene = scene

    def __init_ui_themes(self):
        with open(f'UI/UI_Styles/{self.ui_theme_name}.json') as f:
            file_data = f.readlines()
            for line in file_data:
                try:
                    if line[0] + line[1] == '//':
                        file_data.remove(line)
                except IndexError:
                    pass
            self.ui_theme = ast.literal_eval(''.join(file_data))

    def create_button(self, rel_x, rel_y, rel_width, rel_height, text='', func=print, args=['ButtonPressed']):
        self.ui_elements.append(Button(self, rel_x, rel_y, rel_width, rel_height, text, func, args))

    def create_area(self, rel_x, rel_y, rel_width, rel_height):
        self.ui_elements.append(Area(self, rel_x, rel_y, rel_width, rel_height))

    def create_text(self, rel_x, rel_y, rel_width, rel_height, text='', text_color=raylib.WHITE):
        self.ui_elements.append(Text(self, rel_x, rel_y, rel_width, rel_height, text, text_color))

    def create_slider(self, rel_x, rel_y, rel_width, rel_height, min_value, max_value, initial_value, on_change_func=print, on_change_args=['value changed']):
        self.ui_elements.append(Slider(self, rel_x, rel_y, rel_width, rel_height, min_value, max_value, initial_value, on_change_func, on_change_args))

    def create_checkbox(self, rel_x, rel_y, rel_size, text, initial_checked=False, on_change_func=None, on_change_args=None):
        self.ui_elements.append(Checkbox(self, rel_x, rel_y, rel_size, text, initial_checked, on_change_func, on_change_args))

    def create_input_field(self, rel_x, rel_y, rel_width, rel_height, initial_text="", max_length=100, on_enter_func=None, on_enter_args=None):
        self.ui_elements.append(InputField(self, rel_x, rel_y, rel_width, rel_height, initial_text, max_length, on_enter_func, on_enter_args))

    def create_texture(self, rel_x, rel_y, rel_width, rel_height, texture_name=None, tint=raylib.WHITE):
        self.ui_elements.append(Texture(self, rel_x, rel_y, rel_width, rel_height, texture_name, tint))

    def create_slotlist(self, array, rel_x, rel_y, slot_size, distance_between=5):
        self.ui_elements.append(Slotlist(self, array, rel_x, rel_y, slot_size, distance_between))

    def update(self):
        for element in self.ui_elements:
            element.update()
