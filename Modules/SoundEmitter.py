from Modules.Module import *
import raylib
import math

class SoundEmitter(Module):
    def __init__(self, sound_name, target_object):
        self.inited = False
        self.current_sound_name = sound_name
        self.current_sound = None
        self.target_object = target_object
        self.hearing_range = 150
        self.volume_step = 1 / self.hearing_range
        self.volume = 0.5

    def update(self):
        if not self.inited:
            if not self.parent.get_module('Sprite2D'):
                raise Exception(f'PyLyEngineError: Module "{self.__class__.__name__}" requires "Sprite2D" module')
            if not self.target_object.get_module('Sprite2D'):
                raise Exception(f'PyLyEngineError: Module "{self.__class__.__name__}" requires "Sprite2D" module in target_object')
            self.inited = True

        distance = math.hypot(
            self.parent.x - self.target_object.x,
            self.parent.y - self.target_object.y,
        )
        if distance > self.hearing_range:
            self.volume = 0
        else:
            self.volume = 1 - (distance * self.volume_step)

    def play(self):
        self.current_sound = self.parent.parent_scene.window.source_manager[self.current_sound_name]
        #print(self.volume)
        if self.volume and self.current_sound:
            raylib.SetSoundVolume(self.current_sound, self.volume)
            raylib.PlaySound(self.current_sound)


