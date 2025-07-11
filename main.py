import arcade
from game import Game
from globals import *

"""
If necessary for the sake of clarity Event Handlers (callbacks) 
will be renamed:
    on_draw -> draw
    on_key_press -> keypressed
    on_update -> update
"""

window: arcade.Window = arcade.Window(800, 600, "Typer", center_window=True)
game: Game = Game()

@window.event("on_draw")
def draw() -> None:
    window.clear()
    window.background_color = BG_COLOR
    game.draw()

@window.event("on_key_press")
def keypressed(key: int, _: int) -> None:
    # the second argument (modifiers) won't be necessary
    if key == arcade.key.ESCAPE:
        window.close()
    game.keypressed(key)

@window.event("on_update")
def update(dt: float) -> None:
    game.update(dt)
    
if __name__ == "__main__":
    game.setup()
    window.run()