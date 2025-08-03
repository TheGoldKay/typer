##### 1 - Word overlapping: Check for collision at gen_word *[DONE]*

Started using arcade.Text rather than a simple string, the Text class 
provides all corners of the word's bounding box (left, right, top, bottom), 
and thus it made it easier to check for collisions. The problem with this 
solution is the fact that I get bounding box information after the word has 
been draw/display (even if not visually), thus the collison check happens in 
on_draw() rather than on_update(), if the last one generated collides with any 
other I just delete it, this is a temporary solution until I come up with a better one

##### 2 - Blury text: Updating too fast? Blury display of words *[DONE]*

The old code used float positioning rather than int thus making the words blury due 
to the decimal steps it took each frame

##### 3 - Word stopping at leftmost x side, stopped moving and frozen *[DONE]*

When updating the word position (moving to the left), I was rounding the value to
fix the issue 2 above, but using math.ceil which rounds up to the nearest integer,
thus x never lowers below 0 in some cases, depending where the random x placed it
in the rightmost corner when generated, now I'm using math.floor and also the Check
is to remove any word when: x <= 0, rather than: x < 0, now I made sure it reaches zero
and it doesn't get stuck at the leftmost corner. 

##### 4 - At typing (selecting self.current_word), words outside the screen can get selected *[DONE]*

I have implement two methods: _within_bounds, _current_word_out_of_bounds

Within bounds checks if the word is within the screen bounds, and current_word_out_of_bounds
checks if the current_word is out of bounds (the word selected by the player), if that happens
it is set to 0 (current_word), zero means no word is selected, thus why the value must be
decresed by one everytime I need to index a Word in self.display_words

##### 5 - next current_word isn't selected, unable to lock in other words *[DONE]*

Changed where the check for empty current_word is done to happen right after it has been shorted
by the keypressed (typing), before it never reached the 'if' statement to check for empty because one
was already happeing before back to when I was still only considering the current_word as empty since
None of the words on the screen had been selected yet

The logic above is no longer the cause, it wasn't even when I first wrote it, anyway, current_word is a int
rather than an empty string

##### 6 - Issue with word selection, must fix by forcing selection to the leftmost
##### 7 - More than one word selected at a time, enforce single selection 
##### Fix for 6 & 7 

It seems that in the **update** function, during the looping over the words, the copy of the *display_words*
was being reduced inside the loop, thus in the next iteration the index didn't correspond to the right word
because the copied display words was shorter than the original one, and thus when using *del self.display_words[index]*
the index didn't correspond to the right word, and not only that, in the **keypressed** function getting the *self.focus_word.index*
didn't get the right *focus_word* due to the error mentioned above, therefore I decided to hande the *focus_word* as stand alone
rather than tracking the index of it on *display_words*. 

In order to avoid problems with index I broke out of the loop in **keypressed** and **update** as soon as either a word was selected or
a word was deleted. 