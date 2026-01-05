from Window.Window import *
from Scene.Scene import *
from Objects.Player import *
from Objects.Object import *
from Modules.Sprite2D import *
from Modules.Movement import *
from Animation.Animation import*
from Tilemap.Tilemap import *
import raylib

window = Window(width=1200, height=800)
scene = Scene(window)

tile_map = Tilemap(
    world_width=128,
    world_height=128,
    default_block={'texture': 'cobblestone'},
    layer=0,
    random_flip=True
)

scene.add_object(tile_map)

player = Player()

player.add_module(Sprite2D(animation_name='player_idle_front_animation', layer=1))
player.add_module(Movement())
scene.add_object(player)

scene.camera.set_focus_object(player)

while not raylib.WindowShouldClose():
    scene.update()

raylib.CloseWindow()
