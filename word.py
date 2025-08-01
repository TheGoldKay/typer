from arcade import Text
from globals import * 

class Word(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = FONT_COLOR
        self.font_size = FONT_SIZE
        self.i = 0
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Word): 
            return self.value == other.value
        return False
    
    @property
    def empty(self) -> bool:
        return self.value == ""
    
    @property
    def index(self) -> int:
        return self.i
    
    @index.setter
    def index(self, i: int) -> None:
        self.i = i
    
    def check(self, key: int) -> bool:
        return self.value[0] == chr(key)

    def attack(self) -> None:
        self.value = self.value[1:]
    
    def copy(self, other: object) -> None:
        if isinstance(other, Word):
            self.value = other.value[1:]
            self.x = other.x
            self.y = other.y
            self.color = HIGHLIGHT_COLOR
        else:
            raise TypeError("Object must be of type Word")