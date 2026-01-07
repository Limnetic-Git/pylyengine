import raylib
import ast
import os

class SourceManager:
    def __init__(self):
        self.sources = {}
        print(os.path.dirname(os.path.abspath(__file__)))
        self.__load_source_list()

    def load_animation(self, dir_path, animation_name):
        frames = os.listdir(dir_path)
        animation_frames_list = []
        for frame in frames:
            this_frame_name = frame.split('.')[0]
            self.load_texture(f'{dir_path}/{this_frame_name}.png', this_frame_name)
            animation_frames_list.append(this_frame_name)
        self.sources[animation_name] = animation_frames_list
        #print(f"Loaded anim: {self.sources[animation_name].__dict__} - {animation_name}")

    def load_texture(self, texture_path, texture_name):
        self.sources[texture_name] = raylib.LoadTexture(texture_path.encode())

    def load_sound(self, sound_path, sound_name):
        self.sources[sound_name] = raylib.LoadSound(sound_path.encode())

    def __load_source_list(self):
        with open('Source/source_list.json') as f:
            file_data = f.readlines()
            for line in file_data:
                try:
                    if line[0] + line[1] == '//':
                        file_data.remove(line)
                except IndexError:
                    pass

            data = ast.literal_eval(''.join(file_data))
            
        for key in data:
            if '_animation' in key:
                self.load_animation(data[key], key)
            elif '_sound' in key:
                self.load_sound(data[key], key)
            else:
                self.load_texture(data[key], key)
        
    def __getitem__(self, key):
        return self.sources[key]

