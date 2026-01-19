from Window.Window import *
from Scene.Scene import *
from Objects.Player import *
from Objects.Object import *
from Objects.TestObject import *
from Modules.Sprite2D import *
from Modules.Movement import *
from Modules.SoundEmitter import *
from Animation.Animation import*
from Tilemap.Tilemap import *
from UI.UIScene import *
from Inventory.Inventory import *
from Inventory.Item import *
import raylib

window = Window(width=1200, height=800)
scene = Scene(window)

inv = Inventory(9, 5)
inv.give(Item('Test', 'block', 'test', 16), 300)
inv.give(Item('Test2', 'block', 'rect_test', 16), 300)

scene.add_ui_scene(UIScene())
#scene.ui_scenes[0].create_area(0.1, 0.1, 0.8, 0.8)
#scene.ui_scenes[0].create_slotlist(inv.inventory, 0.2, 0.2, 64)

tile_map = Tilemap(
    world_width=128,
    world_height=128,
    default_block={'texture': 'cobblestone', 'solid': True},
    layer=0,
    random_flip=True
)
tile_map.world[10][0] = {'texture': 'rect_test', 'solid': False, 'flip_x': False, 'flip_y': False}

scene.add_object(tile_map)

player = Player()


player.add_module(Sprite2D(animation_name='player_idle_front_animation', layer=1))
player.add_module(Movement())
scene.add_object(player)

test = TestObject()
test.add_module(Sprite2D(animation_name='player_idle_front_animation', layer=2))
test.add_module(SoundEmitter(sounds_names=['test_sound'], target_object=player))
scene.add_object(test)

scene.camera.set_focus_object(player)

while not raylib.WindowShouldClose():
    scene.update()

raylib.CloseWindow()
