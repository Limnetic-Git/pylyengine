from Window.Window import *
from Scene.Scene import *
from Objects.Player import *
from Objects.Object import *
from Modules.Sprite2D import *
from Modules.Movement import *
from Animation.Animation import*
from Tilemap.Tilemap import *
import raylib

window = Window(1200, 800)
scene = Scene(window)


tile_map = Tilemap(10, 10, {'texture': 'cobblestone'}, layer=0)
scene.add_object(tile_map)

player = Player()
player_run_animation = Animation(['0', '1', '2', '3'], 8)
player.add_module(Sprite2D(animation=player_run_animation, layer=1))
player.add_module(Movement())
scene.add_object(player)


scene.camera.set_focus_object(player)

test = Object()
test_idle_animation = Animation(['cobblestone'])
test.add_module(Sprite2D(test_idle_animation))
test.scale_x = 2.0
test.scale_y = 2.0
scene.add_object(test)


while not raylib.WindowShouldClose():
    tile_map.update()
    scene.update()

raylib.CloseWindow()
