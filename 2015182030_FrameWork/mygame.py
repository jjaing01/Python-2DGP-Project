import game_framework
import pico2d

import start_state

# fill here
pico2d.open_canvas(1080,600,sync=True)
game_framework.run(start_state)
pico2d.close_canvas()
