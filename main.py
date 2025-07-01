import arcade
from globals import *

"""
If necessary for the sake of clarity Event Handlers (callbacks) 
will be renamed:
    on_draw -> draw
    on_key_press -> keypressed
"""

window: arcade.Window = arcade.Window(800, 600, "Typer", center_window=True)

@window.event("on_draw")
def draw() -> None:
    window.clear()
    window.background_color = BG_COLOR

@window.event("on_key_press")
def keypressed(key: int, _: int) -> None:
    # the second argument (modifiers) won't be necessary
    if key == arcade.key.ESCAPE:
        window.close()
    
if __name__ == "__main__":
    window.run()