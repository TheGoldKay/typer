import random
import math
import time
from dataclasses import dataclass, field
from pyglet.graphics import Batch
from arcade import Text
from word import Word
from globals import *

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
        if self.current_word == 0:
            selection: list[Word] = []
            for index, word in enumerate(self.display_words):
                #print(word.value[0], chr(key).lower())
                if word.value[0] == chr(key).lower() and self._within_bounds(word):
                    word.index = index
                    word.value = word.value[1:]
                    word.color = HIGHLIGHT_COLOR
                    selection.append(word)
            if len(selection) >= 1:
                #print(selection)
                leftmost: Word = min(selection, key=lambda w: w.x)
                self.current_word = leftmost.index + 1
                #print(leftmost.value)
        else:
            word = self.display_words[self.current_word - 1]
            if word.check(key):
                word.attack()
                if word.empty:
                    del self.display_words[word.index]
                    self.current_word = 0
                else:
                    self.display_words[word.index].value = word.value
    
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