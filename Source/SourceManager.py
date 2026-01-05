import raylib
import ast
import os


class SourceManager:
    def __init__(self):
        self.sources = {}
        print(os.path.dirname(os.path.abspath(__file__)))
        self.__load_source_list()
        
    def load_texture(self, texture_path, texture_name):
        self.sources[texture_name] = raylib.LoadTexture(texture_path.encode('utf-8'))

    def __load_source_list(self):
        with open('Source/source_list.json') as f:
            data = ast.literal_eval(''.join(f.readlines()))
            
        for key in data:
            self.load_texture(data[key], key)
        
    def __getitem__(self, key):
        return self.sources[key]

