from dataclasses import dataclass, field
import random, arcade, math, time
from pyglet.graphics import Batch
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
    
    def copy(self, other: object) -> None:
        if isinstance(other, Word):
            self.value = other.value[1:]
            self.x = other.x
            self.y = other.y
            self.color = HIGHLIGHT_COLOR
        else:
            raise TypeError("Object must be of type Word")

@dataclass
class Game:
    word_list: list[str] = field(default_factory=lambda: 
        list(DEFAULT_WORD_LIST).copy())
    score: int = 0
    lives: int = 3
    range_len: tuple[int, int] = 3, 15 # both ends included
    max_words: int = 8
    gap: int = FONT_SIZE + 10
    vel_word: int = 150
    batch: Batch = field(default_factory=Batch)
    display_words: list[Word] = field(default_factory=list)
    
    def setup(self):
        random.seed(time.time())
        random.shuffle(self.word_list)
        # the first word is set to self.current_word == 1 (not following index 0 convention) 
        self.current_word: int = 0 
        self.gen_word()
        
    def gen_word(self) -> None:
        if (len(self.display_words) == self.max_words):
            return
        # check if it's within the range for length and if there are less than max words allowed
        while True:
            word: str = random.choice(self.word_list)
            if self.range_len[0] <= len(word) <= self.range_len[1] and self._is_unique(word):
                self.display_words.append(Word(word, 
                        random.randint(SCREEN_WIDTH, SCREEN_WIDTH + self.gap * 15),
                        random.randint(self.gap, SCREEN_HEIGHT - self.gap), 
                        batch = self.batch))
                return
    def _is_unique(self, word: str) -> bool:
        # return all(w.value != word for w in self.display_words)
        for w in self.display_words:
            if not w.empty and w.value[0] == word[0]:
                return False
        return True
    
    def _not_nique(self, word: str) -> bool:
        return any(w.value == word for w in self.display_words)
    
    def _word_collision(self, new_last_word: Text) -> bool:
        for word in self.display_words[:-1]: # all except the last one (being checked)
            if (
                new_last_word.left < word.right and
                new_last_word.right > word.left and
                new_last_word.bottom < word.top and
                new_last_word.top > word.bottom
            ):
                return True
        return False    
    
    def _within_bounds(self, word: Word) -> bool:
        return 0 < word.x < SCREEN_WIDTH and 0 < word.y < SCREEN_HEIGHT
    
    def keypressed(self, key: int) -> None:
        if not self.current_word:
            selection: list[Word] = []
            for index, word in enumerate(self.display_words):
                #print(word.value[0], chr(key).lower())
                if word.value[0] == chr(key).lower() and self._within_bounds(word):
                    word.index = index
                    word.value = word.value[1:]
                    word.color = HIGHLIGHT_COLOR
                    selection.append(word)
            if len(selection) >= 1:
                leftmost: Word = min(selection, key=lambda w: w.x)
                self.current_word = leftmost.index + 1
                print(leftmost.value)
        else:
            word = self.display_words[self.current_word - 1]
            if word.check(key):
                self.display_words[self.current_word - 1].value = word.value[1:]
                if self.display_words[self.current_word - 1].empty:
                    del self.display_words[self.current_word - 1]
                    self.current_word = 0

    
    def _current_word_out_of_bounds(self) -> bool:
        return not self._within_bounds(self.display_words[self.current_word - 1])
    
    def update(self, dt: float) -> None:
        self.gen_word()
        display_words_copy = self.display_words.copy()
        for i, word in enumerate(self.display_words):
            word.x -= math.floor(self.vel_word * dt)
            if word.x <= 0:
                if i == self.current_word - 1:
                    self.current_word = 0
                del display_words_copy[i]
        self.display_words = display_words_copy
    
    def draw(self) -> None:
        self.batch.draw()
        if self._word_collision(self.display_words[-1]):
            del self.display_words[-1]