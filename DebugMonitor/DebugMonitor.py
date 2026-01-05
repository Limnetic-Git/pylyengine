import raylib
import os
import psutil

class DebugMonitor:
    def __init__(self):
        self.drawing_objects_count = 0
        self.process = psutil.Process()

    def update(self):
        raylib.DrawText(f"FPS: {raylib.GetFPS()}".encode(), 5, 5, 20, raylib.LIME)
        raylib.DrawText(f"Draw calls: {self.drawing_objects_count}".encode(), 5, 28, 20, raylib.LIME)

        rss = round(self.process.memory_info().rss / 1024 / 1024, 2)
        raylib.DrawText(f"RSS: {rss}Mb".encode(), 5, 51, 20, raylib.RED)

        self.drawing_objects_count = 0

