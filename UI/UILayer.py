from UI.UI_Elements.Button import *
from UI.UI_Elements.Area import *
from UI.UI_Elements.Text import *
from UI.UI_Elements.Slider import *
import ast
import os

class UILayer:
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
    def create_text(self, rel_x, rel_y, rel_width, rel_height, text=''):
        self.ui_elements.append(Text(self, rel_x, rel_y, rel_width, rel_height, text))
    def create_slider(self, rel_x, rel_y, rel_width, rel_height, min_value, max_value, initial_value, on_change_func=print, on_change_args=['value changed']):
        self.ui_elements.append(Slider(self, rel_x, rel_y, rel_width, rel_height, min_value, max_value, initial_value, on_change_func, on_change_args))

    def update(self):
        for element in self.ui_elements:
            element.update()
