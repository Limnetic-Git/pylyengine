class Object:
    def __init__(self):
        self.modules = []

    def set_parent_scene(self, scene):
        self.parent_scene = scene
        
    def add_module(self, module):
        module.set_parent(self)
        self.modules.append(module)
    
    def get_module(self, module_name):
        for module in self.modules:
            if module.__class__.__name__ == module_name:
                return module
    
    def update(self):
        for module in self.modules:
            module.update()
    
        
