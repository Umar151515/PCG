from .collision_shapes import Rect
from .window_console import WindowConsole


__all__ = ['TextImage', 'Surface']


class TextImage():
    def __init__(self, text: str):
        self.text = text
        self._check_text_image(text)

        self.image_shares = text.split('\n')
        
        self.size_x = len(max(self.image_shares, key=len))
        self.size_y = len(self.image_shares)

    def _check_text_image(self, new_text):
        if not isinstance(new_text, str):
            raise TypeError('text должен быть строкой.')
        if not new_text:
            raise TypeError('text не должен быть пустым.')
    
    @property
    def size(self):
        return self.size_x, self.size_y
        
    def get_rect(self):
        return Rect(0, 0, text_image = self)
    

class Surface(WindowConsole, TextImage):
    '''
    Наследуется от WindowConsole и TextImage и является их совокупностью
    Его можно рисовать на консоли и рисовать на нём
    '''
    def __init__(self, size_x: int, size_y: int):
        super().__init__(size_x, size_y)

    def update(self):
        self.text = ''

        for texts in self.field:
            self.text += ''.join(texts)
        