import time


__all__ = ['FPS']


class FPS:
    '''Выводит и ограничивает FPS'''
    def __init__(self, desired_fps: int):
        '''desired_fps: int ограничивает FPS'''
        desired_fps = max(desired_fps, 1e-3)
        desired_fps = min(desired_fps, 600)

        self._desired_fps = desired_fps
        self._desired_frame_time = 1 / desired_fps

        self._frames = 0
        self._start_time_get_fps = time.time()
        self._start_time_delay = time.time()
    
    @property
    def desired_fps(self):
        return self.desired_fps
    
    @desired_fps.setter
    def desired_fps(self, fps):
        self._desired_fps = fps
        self._desired_frame_time = 1 / fps

    @property
    def program_running_time(self):
        return time.time() - self._start_time_get_fps

    def get_fps(self):
        self._frames += 1

        elapsed_time = self.program_running_time
        elapsed_time = max(elapsed_time, 1e-10)
        fps = self._frames / elapsed_time

        return fps

    def delay(self):
        elapsed_time = time.time() - self._start_time_delay
        remaining_time = self._desired_frame_time - elapsed_time

        if remaining_time > 0:
            time.sleep(remaining_time)

        self._start_time_delay = time.time()