##### 1 - Word overlapping: Check for collision at gen_word [DONE]

Started using arcade.Text rather than a simple string, the Text class 
provides all corners of the word's bounding box (left, right, top, bottom), 
and thus it made it easier to check for collisions. The problem with this 
solution is the fact that I get bounding box information after the word has 
been draw/display (even if not visually), thus the collison check happens in 
on_draw() rather than on_update(), if the last one generated collides with any 
other I just delete it, this is a temporary solution until I come up with a better one

##### 2 - Blury text: Updating too fast? Blury display of words [DONE]

The old code used float positioning rather than int thus making the words blury due 
to the decimal steps it took each frame

##### 3 - Word stopping at leftmost x side, stopped moving and frozen [DONE]

When updating the word position (moving to the left), I was rounding the value to
fix the issue 2 above, but using math.ceil which rounds up to the nearest integer,
thus x never lowers below 0 in some cases, depending where the random x placed it
in the rightmost corner when generated, now I'm using math.floor and also the Check
is to remove any word when: x <= 0, rather than: x < 0, now I made sure it reaches zero
and it doesn't get stuck at the leftmost corner. 

##### 4 - At typing (selecting self.current_word), words outside the screen can get selected []