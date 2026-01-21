from Modules.Module import *
import raylib

class Movement(Module):
    def __init__(self):
        self.inited = False

    def update(self):
        if not self.inited:
            if not self.parent.get_module('Sprite2D'):
                raise Exception(f'PyLyEngineError: Module "{self.__class__.__name__}" requires "Sprite2D" module')
            if not hasattr(self.parent, 'speed'):
                self.parent.speed = 1
            self.inited = True

        speed = self.parent.speed

        move_keys = [raylib.IsKeyDown(raylib.KEY_W),
                     raylib.IsKeyDown(raylib.KEY_A),
                     raylib.IsKeyDown(raylib.KEY_S),
                     raylib.IsKeyDown(raylib.KEY_D)]
        if any(move_keys):
            last_moves = []
            for object in self.parent.parent_scene.objects:
                if hasattr(object, 'name') and object.name == 'tilemap':
                    player_x, player_y = self.parent.x + 5, self.parent.y + 20
                    last_tile_under_player_cords = object.get_tile_cords_under(player_x, player_y)
            if raylib.IsKeyDown(raylib.KEY_W):
                self.parent.y -= self.parent.speed
                last_moves.append([0, -self.parent.speed])
            if raylib.IsKeyDown(raylib.KEY_A):
                self.parent.x -= self.parent.speed
                last_moves.append([-self.parent.speed, 0])
            if raylib.IsKeyDown(raylib.KEY_S):
                self.parent.y += self.parent.speed
                last_moves.append([0, self.parent.speed])
            if raylib.IsKeyDown(raylib.KEY_D):
                self.parent.x += self.parent.speed
                last_moves.append([self.parent.speed, 0])
            for object in self.parent.parent_scene.objects:
                if hasattr(object, 'name') and object.name == 'tilemap':
                    player_x, player_y = self.parent.x + 5, self.parent.y + 20
                    tile_under_player_cords = object.get_tile_cords_under(player_x, player_y)
                    distance = abs(last_tile_under_player_cords[0] - tile_under_player_cords[0]) + \
                               abs(last_tile_under_player_cords[1] - tile_under_player_cords[1])
                    if distance >= 2:
                        for move in last_moves:
                            self.parent.x -= move[0]
                            self.parent.y -= move[1]
                    elif object.world[tile_under_player_cords[0]][tile_under_player_cords[1]]['solid']:
                        for move in last_moves:
                            self.parent.x -= move[0]
                            self.parent.y -= move[1]


