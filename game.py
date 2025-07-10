from dataclasses import dataclass, field
import random, arcade, math
from pyglet.graphics import Batch
from arcade import Text
from globals import *

        
@dataclass
class Game:
    word_list: tuple[str, ...] = DEFAULT_WORD_LIST
    current_word: str = ""
    score: int = 0
    lives: int = 3
    range_len: tuple[int, int] = 3, 5 # both ends included
    max_words: int = 20
    gap: int = FONT_SIZE + 10
    vel_word: int = 100
    batch: Batch = field(default_factory=Batch)
    display_words: list[Text] = field(default_factory=list)
    
    def gen_word(self) -> None:
        if (len(self.display_words) == self.max_words):
            return
        word: str = random.choice(self.word_list)
        # check if it's within the range for length and if there are less than max words allowed
        if self.range_len[0] <= len(word) <= self.range_len[1]:
            w: Text = Text(word, 
                    random.randint(SCREEN_WIDTH, SCREEN_WIDTH + self.gap * 15),
                    random.randint(self.gap, SCREEN_HEIGHT - self.gap), 
                    batch = self.batch, 
                    font_size = FONT_SIZE,
                    color = FONT_COLOR)
            if not self._is_unique(w):
                self.gen_word()
            else:
                self.display_words.append(w)
        else:
            self.gen_word()
    def _is_unique(self, word: Text) -> bool:
        return word not in self.display_words
    
    def _word_collision(self, new_word: Text) -> bool:
        for word in self.display_words[:-1]:
            if (
                new_word.left < word.right and
                new_word.right > word.left and
                new_word.bottom < word.top and
                new_word.top > word.bottom
            ):
                return True
        return False     
            
    def update(self, dt: float) -> None:
        self.gen_word()
        display_words_copy = self.display_words.copy()
        for i, word in enumerate(self.display_words):
            word.x -= math.ceil(self.vel_word * dt)
            if word.x < 0:
                del display_words_copy[i]
        self.display_words = display_words_copy
    
    def draw(self) -> None:
        self.batch.draw()
        if self._word_collision(self.display_words[-1]):
            del self.display_words[-1]