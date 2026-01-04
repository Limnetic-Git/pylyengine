import Extentions.raylib_extention as raylib_ex

class Tilemap:
    def __init__(self, scene, world_width, world_height, default_block):
        self.parent_scene = scene
        self.world_width = world_width
        self.world_height = world_height
        self.default_block = default_block
        self.block_scale_x = 1.0
        self.block_scale_y = 1.0

        self.world = [[default_block for _ in range(world_height)] for __ in range(world_width)]

    def update(self):
        for x in range(self.world_width):
            for y in range(self.world_height):
                texture = self.parent_scene.window.source_manager[self.default_block['texture']]
                raylib_ex.DrawTexture(
                    texture=texture,
                    position=(x * texture.width, y * texture.height),
                    rotation=0,
                    scale=(self.block_scale_x, self.block_scale_y),
                    window=self.parent_scene.window,
                    camera=self.parent_scene.camera,
                    )

