import os
import pico2d
import play_state
import logo_state

start_state = logo_state # 모듈을 변수로 취급

os.chdir(os.path.dirname(__file__))

pico2d.open_canvas(sync=True)
start_state.enter()

# # game main loop code
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     if start_state.running == False:
#         if start_state == logo_state:
#             start_state.exit()
#             start_state = play_state
#         elif start_state == play_state:
#             start_state.exit()
#             break
#         start_state.enter()
states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

# finalization code
pico2d.close_canvas()
