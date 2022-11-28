import game_framework
import pico2d
import os

import play_state

os.chdir(os.path.dirname(__file__))

pico2d.open_canvas(1600, 600)
game_framework.run(play_state)
pico2d.close_canvas()