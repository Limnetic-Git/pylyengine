import Extentions.raylib_extention as raylib_ex
from Objects.Object import *
import random

class Tilemap(Object):
    def __init__(self, world_width, world_height, default_block, layer=0):
        self.name = 'tilemap'

        self.layer_id = layer
        self.world_width = world_width
        self.world_height = world_height
        self.default_block = default_block

        self.random_flip = True
        self.block_scale_x = 1.5
        self.block_scale_y = 1.5

        self.world = [[default_block.copy() for _ in range(world_height)] for __ in range(world_width)]
        for x in range(self.world_width):
            for y in range(self.world_height):
                self.world[x][y]['flip_x'] = random.choice([True, False])
                self.world[x][y]['flip_y'] = random.choice([True, False])
        super().__init__()

    def update(self):
        for x in range(self.world_width):
            for y in range(self.world_height):
                texture = self.parent_scene.window.source_manager[self.default_block['texture']]
                #print(self.world[x][y])
                raylib_ex.DrawTexture(
                    texture=texture,
                    position=(x * texture.width * self.block_scale_x,
                              y * texture.height * self.block_scale_y),
                    rotation=0,
                    scale=(self.block_scale_x, self.block_scale_y),
                    window=self.parent_scene.window,
                    camera=self.parent_scene.camera,
                    flip_x=self.world[x][y]['flip_x'],
                    flip_y=self.world[x][y]['flip_y'],
                    )


        #super().update()

