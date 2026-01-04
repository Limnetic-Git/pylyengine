import raylib

class DebugMonitor:
    def __init__(self):
        self.drawing_objects_count = 0

    def update(self):
        raylib.DrawText(f"FPS: {raylib.GetFPS()}".encode(), 5, 5, 20, raylib.DARKGRAY)
        raylib.DrawText(f"Draw calls: {self.drawing_objects_count}".encode(), 5, 28, 20, raylib.DARKGRAY)
        self.drawing_objects_count = 0
