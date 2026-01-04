import raylib
from Source.SourceManager import *
from DebugMonitor.DebugMonitor import *

class Window:
    def __init__(self, width: int, height: int):
        self.MAX_FPS = 60
        self.width = width
        self.height = height
        self.debug_monitor = DebugMonitor()
        
        raylib.InitWindow(width, height, f"Game".encode())
        raylib.SetTargetFPS(self.MAX_FPS)
        
        self.source_manager = SourceManager()


        
