from Window.Window import *
from Scene.Scene import *
from Objects.Player import *
from Objects.Object import *
from Modules.Sprite2D import *
from Modules.Movement import *
import raylib

window = Window(1200, 800)
scene = Scene(window)

player = Player()
player.add_module(Sprite2D(['0', '1', '2', '3'], 8, 1))
player.add_module(Movement())
scene.add_object(player)


scene.camera.set_focus_object(player)

test = Object()
test.add_module(Sprite2D(['rect_test']))
scene.add_object(test)


while not raylib.WindowShouldClose():
    scene.update()


raylib.CloseWindow()

