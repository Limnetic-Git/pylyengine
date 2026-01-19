import Extentions.raylib_extention as raylib_ex
from Objects.Object import *
import random

class Tilemap(Object):
    def __init__(self, world_width, world_height, default_block, layer=0, random_flip=False):
        super().__init__()
        self.name = 'tilemap'
        self.layer_id = layer
        self.world_width = world_width
        self.world_height = world_height
        self.default_block = default_block
        self.random_flip = random_flip
        self.block_scale_x = 1.5
        self.block_scale_y = 1.5

        self.world = [[default_block.copy() for _ in range(world_height)]
                      for __ in range(world_width)]

        if random_flip:
            for row in self.world:
                for block in row:
                    block['flip_x'] = random.choice([True, False])
                    block['flip_y'] = random.choice([True, False])

    def update(self):
        camera = self.parent_scene.camera
        window = self.parent_scene.window


        screen_to_world_x = lambda sx: (sx - camera.x) / camera.zoom_x
        screen_to_world_y = lambda sy: (sy - camera.y) / camera.zoom_y

        texture = window.source_manager[self.default_block['texture']]
        world_left = screen_to_world_x(0)
        world_top = screen_to_world_y(0)
        world_right = screen_to_world_x(window.width)
        world_bottom = screen_to_world_y(window.height)
        tex_width = texture.width * self.block_scale_x
        tex_height = texture.height * self.block_scale_y
        start_x = max(0, int(world_left // tex_width) - 1)
        start_y = max(0, int(world_top // tex_height) - 1)
        end_x = min(self.world_width, int(world_right // tex_width) + 2)
        end_y = min(self.world_height, int(world_bottom // tex_height) + 2)

        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                block = self.world[x][y]
                texture = window.source_manager[block['texture']]
                tex_width = texture.width * self.block_scale_x
                tex_height = texture.height * self.block_scale_y

                start_x = max(0, int(world_left // tex_width) - 1)
                start_y = max(0, int(world_top // tex_height) - 1)
                end_x = min(self.world_width, int(world_right // tex_width) + 2)
                end_y = min(self.world_height, int(world_bottom // tex_height) + 2)

                if not self.random_flip:
                    block['flip_x'], block['flip_y'] = False, False

                if block['texture']:
                    raylib_ex.DrawTexture(
                        texture=texture,
                        position=(x * tex_width, y * tex_height),
                        rotation=0,
                        scale=(self.block_scale_x, self.block_scale_y),
                        window=window,
                        camera=camera,
                        flip_x=block['flip_x'],
                        flip_y=block['flip_y'],
                    )
    def get_tile_cords_under(self, x, y):
        window = self.parent_scene.window
        texture = window.source_manager[self.default_block['texture']]
        return [(x + texture.width // 2) // (texture.width *  self.block_scale_x),
                (y + texture.height // 2) // (texture.height * self.block_scale_y)]
