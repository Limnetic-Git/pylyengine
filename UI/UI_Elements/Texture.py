import raylib

class Texture:
    def __init__(self, ui_layer, rel_x, rel_y, rel_width, rel_height, texture_name, tint):
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.texture_name = texture_name
        self.texture = self.ui_layer.parent_scene.window.source_manager[texture_name]

        self.color = tint
        self.update_position()

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)

    def update(self):
        self.update_position()
        if self.texture:
            source_rect = [0, 0, self.texture.width, self.texture.height]
            dest_rect = [self.x, self.y, self.width, self.height]
            origin = [0, 0]
            rotation = 0

            raylib.DrawTexturePro(
                self.texture,
                source_rect,
                dest_rect,
                origin,
                rotation,
                self.color
            )
        else:
            raylib.DrawRectangle(
                self.x,
                self.y,
                self.width,
                self.height,
                self.color
            )
