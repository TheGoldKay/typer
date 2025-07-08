from dataclasses import dataclass
import random
from globals import *


@dataclass
class Game:
    word_list: tuple[str, ...] = DEFAULT_WORD_LIST
    current_word: str = ""
    score: int = 0
    lives: int = 3
    range_len: tuple[int, int] = 3, 5 # both ends included
    def gen_word(self) -> None:
        word: str = random.choice(self.word_list)
        if self.range_len[0] <= len(word) <= self.range_len[1]:
            self.current_word = word
        else:
            self.gen_word()