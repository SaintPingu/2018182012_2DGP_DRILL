from pico2d import *

os.chdir(os.path.dirname(__file__))

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

boy = None
grass = None
running = True

def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

def exit():
    global boy, grass, running
    del boy
    del grass

def update():
    global boy
    boy.update()

def draw():
    global boy, grass
    clear_canvas()
    boy.draw()
    grass.draw()
    update_canvas()


open_canvas()
enter()

# game main loop code
while running:
    handle_events()
    update()
    draw()
    delay(0.05)

# finalization code
exit()
close_canvas()
