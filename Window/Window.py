import raylib
from Source.SourceManager import *
from DebugMonitor.DebugMonitor import *

class Window:
    def __init__(self, width: int, height: int):
        self.MAX_FPS = 60
        self.width = width
        self.height = height
        self.debug_monitor = DebugMonitor()
        self.mouse_x = 0
        self.mouse_y = 0
        
        raylib.InitWindow(width, height, f"My game on PyLyEngine".encode())
        raylib.SetTargetFPS(self.MAX_FPS)
        raylib.SetWindowState(raylib.FLAG_WINDOW_RESIZABLE)
        raylib.InitAudioDevice()

        self.source_manager = SourceManager()

    def update(self):
        self.mouse_x = raylib.GetMouseX()
        self.mouse_y = raylib.GetMouseY()



        
