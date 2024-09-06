import ctypes

from .window_console import WindowConsole


__all__ = ['Mouse']


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


class Mouse:
    @staticmethod
    def get_mouse_position():
        pt = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        return pt.x, pt.y