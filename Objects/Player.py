from Objects.Object import *
import raylib
from Animation.Animation import *

class Player(Object):
    def __init__(self):
        super().__init__()
        self.name = 'player'
        self.speed = 2

        self.scale_x = 1.75
        self.scale_y = 1.75


    def update(self):
        super().update()
        sprite2d_module = self.get_module('Sprite2D')

        move_keys = [raylib.IsKeyDown(raylib.KEY_W),
                     raylib.IsKeyDown(raylib.KEY_A),
                     raylib.IsKeyDown(raylib.KEY_S),
                     raylib.IsKeyDown(raylib.KEY_D)]

        self.flip_x = False

        if any(move_keys):
            if raylib.IsKeyDown(raylib.KEY_A):
                self.flip_x = True
                if sprite2d_module.animation_name != 'player_run_side_animation':
                    sprite2d_module.animation_name = 'player_run_side_animation'

            if raylib.IsKeyDown(raylib.KEY_D):
                if sprite2d_module.animation_name != 'player_run_side_animation':
                    sprite2d_module.animation_name = 'player_run_side_animation'

            if raylib.IsKeyDown(raylib.KEY_W):
                if sprite2d_module.animation_name != 'player_run_back_animation':
                    sprite2d_module.animation_name = 'player_run_back_animation'

            if raylib.IsKeyDown(raylib.KEY_S):
                if sprite2d_module.animation_name != 'player_run_front_animation':
                    sprite2d_module.animation_name = 'player_run_front_animation'

        else:
            if sprite2d_module.animation_name != 'player_idle_front_animation':
                sprite2d_module.animation_name = 'player_idle_front_animation'

        if raylib.IsKeyPressed(raylib.KEY_E):
            for object in self.parent_scene.objects:
                if hasattr(object, 'name') and object.name == 'tilemap':
                    x, y = self.x, self.y
                    print(object.get_tile_cords_under(x, y))
        if raylib.IsMouseButtonReleased(0):
            x = self.parent_scene.camera.mouse_x + 6
            y = self.parent_scene.camera.mouse_y + 6
            for object in self.parent_scene.objects:
                if hasattr(object, 'name') and object.name == 'tilemap':
                    bx, by = object.get_tile_cords_under(x, y)
                    if object.world[bx][by]['texture'] == 'cobblestone':
                        object.world[bx][by]['texture'] = 'cobblestone_1'
                    elif object.world[bx][by]['texture'] == 'cobblestone_1':
                        object.world[bx][by]['texture'] = 'cobblestone_2'
                    elif object.world[bx][by]['texture'] == 'cobblestone_2':
                        object.world[bx][by]['texture'] = 'rect_test'
                        object.world[bx][by]['solid'] = False





