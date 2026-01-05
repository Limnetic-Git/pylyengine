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


tile_map = Tilemap(128, 128, {'texture': 'cobblestone'}, layer=0)
scene.add_object(tile_map)

player = Player()
player_idle_front_animation = Animation(['idle_front_0', 'idle_front_1', 'idle_front_2', 'idle_front_3'], 8)

player.add_module(Sprite2D(animation=player_idle_front_animation, layer=1))
player.add_module(Movement())
scene.add_object(player)

scene.camera.set_focus_object(player)


while not raylib.WindowShouldClose():
    scene.update()


raylib.CloseWindow()
