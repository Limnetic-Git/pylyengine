import raylib

class Slotlist:
    def __init__(self, ui_layer, array, rel_x, rel_y, slot_size, distance_between=5):
        self.array = array
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = slot_size / 1920 #self.ui_layer.parent_scene.window.width
        self.rel_height = slot_size / 1080 #self.ui_layer.parent_scene.window.height
        self.distance_between = distance_between

        self.selected_slot = [0, 0]


    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)

    def update(self):
        self.update_position()
        for x in range(len(self.array)):
            for y in range(len(self.array[x])):
                raylib.DrawRectangleRounded(
                    [self.x + x * (self.width + self.distance_between),
                     self.y + y * (self.height + self.distance_between),
                     self.width, self.height],
                    0.25,
                    25,
                    [35, 35, 50, 255],
                    )
                if [x, y] == self.selected_slot:
                    raylib.DrawRectangleRoundedLinesEx(
                        [self.x + x * (self.width + self.distance_between),
                        self.y + y * (self.height + self.distance_between),
                        self.width, self.height],
                        0.25,
                        25,
                        3,
                        raylib.RAYWHITE,
                        )

