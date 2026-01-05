class Animation:
    def __init__(self, frames, source_manager, frame_delay=1):
        self.source_manager = source_manager
        self.frames = frames
        self.frame_delay = frame_delay
        self.current_frame_index = 0
        self.animation_tick = 0

    def get_current_frame(self):
        self.animation_step()
        return self.source_manager[self.frames[self.current_frame_index]]

    def animation_step(self):
        if len(self.frames) > 1:
            self.animation_tick += 1
            if self.animation_tick % self.frame_delay == 0:
                self.animation_tick = 0
                if self.current_frame_index == len(self.frames) - 1:
                    self.current_frame_index = 0
                else:
                    self.current_frame_index += 1
