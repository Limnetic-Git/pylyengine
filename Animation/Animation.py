class Animation:
    def __init__(self, frames, frame_delay=1):
        self.frames = frames
        self.frame_delay = frame_delay
        self.current_frame_index = 0
        self.animation_tick = 0

    def get_current_frame(self):
        if len(self.frames) > 1:
            self.animation_tick += 1
            if self.animation_tick % self.frame_delay == 0:
                self.animation_tick = 0
                if self.current_frame_index == len(self.frames) - 1:
                    self.current_frame_index = 0
                else:
                    self.current_frame_index += 1
            return self.frames[self.current_frame_index]
        else:
            return self.frames[0]
