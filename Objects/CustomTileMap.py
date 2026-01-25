import raylib
import math
from Tilemap.Tilemap import *


class CustomTileMap(Tilemap):
    def __init__(self, world_width, world_height, default_block, layer=0, random_flip=False):
        super().__init__(world_width, world_height, default_block, layer, random_flip)
        self.overloaded_world = [[None for _ in range(world_height)]
                      for __ in range(world_width)]
        self.now_loaded = [[False for _ in range(world_height)]
                      for __ in range(world_width)]

    def load_world_around(self, block_x, block_y, rect_side_len):
        for i in [-1, 1]:
            for k in [-1, 1]:
                for j in range(rect_side_len):
                    for u in range(rect_side_len):
                        cx, cy = block_x + (j*i), block_y + (u*k)
                        if j == rect_side_len - 1:
                            if u == rect_side_len - 1:
                                continue
                        not_solids_near = [not i['solid'] for i in self.get_blocks_around(cx, cy)]
                        if any(not_solids_near):
                            self.overloaded_world[cx][cy] = True
                            self.now_loaded[cx][cy] = True

    def get_blocks_around(self, block_x, block_y):
        blocks_around = []
        for left_right in [-1, 0, 1]:
            for up_down in [-1, 0, 1]:
                blocks_around.append(self.world[block_x + left_right][block_y + up_down])
        return blocks_around

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

                flip_x, flip_y = block['flip_x'], block['flip_y']
                tint = raylib.WHITE
                if not self.overloaded_world[x][y]:
                    texture = window.source_manager['unknown_block']
                    flip_x, flip_y = False, False
                else:
                    if not self.now_loaded[x][y]:
                        tint = [150, 150, 150, 255]

                raylib_ex.DrawTexture(
                    texture=texture,
                    position=(x * tex_width, y * tex_height),
                    rotation=0,
                    scale=(self.block_scale_x, self.block_scale_y),
                    window=window,
                    camera=camera,
                    flip_x=flip_x,
                    flip_y=flip_y,
                    tint=tint,
                )
                self.now_loaded[x][y] = False

