from dataclasses import dataclass, field
import random, arcade
from globals import *

class Word:
    def __init__(self, word: str, pos: list[float]):
        self.word: str = word
        self.pos: list[float] = pos
    
    @property
    def x(self) -> float: 
        return self.pos[0]
        
    @x.setter
    def x(self, value: float) -> None:
        self.pos[0] = value
        
@dataclass
class Game:
    word_list: tuple[str, ...] = DEFAULT_WORD_LIST
    current_word: str = ""
    score: int = 0
    lives: int = 3
    range_len: tuple[int, int] = 3, 5 # both ends included
    max_words: int = 5
    gap: int = 100
    vel_word: int = 100
    display_words: list[Word] = field(default_factory=list)
    
    def gen_word(self) -> None:
        if (len(self.display_words) == self.max_words):
            return
        word: str = random.choice(self.word_list)
        # check if it's within the range for length and if there are less than max words allowed
        if self.range_len[0] <= len(word) <= self.range_len[1]:
            self.display_words.append(
                Word(word, [
                    SCREEN_WIDTH,
                    random.randint(self.gap, SCREEN_HEIGHT - self.gap)
                ]))  
        else:
            self.gen_word()
    
    def update(self, dt: float) -> None:
        self.gen_word()
        display_words_copy = self.display_words.copy()
        for i, word in enumerate(self.display_words):
            word.x -= self.vel_word * dt
            if word.x < 0:
                   del display_words_copy[i]
        self.display_words = display_words_copy
    
    def draw(self) -> None:
        for word in self.display_words:
            arcade.draw_text(word.word, word.x, word.pos[1], arcade.color.WHITE, 20)