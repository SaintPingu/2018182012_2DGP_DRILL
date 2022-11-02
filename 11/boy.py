from pico2d import *

RD, LD, RU, LU, TIMER, KEY_A = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT)  : LD,
    (SDL_KEYUP, SDLK_RIGHT)   : RU,
    (SDL_KEYUP, SDLK_LEFT)    : LU,
    (SDL_KEYDOWN, SDLK_a)    : KEY_A,
}


class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    def exit(self):
        print('EXIT IDLE')

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer <= 0:
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')

    def exit(self):
        print('EXIT SLEEP')

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO_RUN')
        self.dir = self.face_dir

    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir
        self.dir = 0

    def do(self):
        self.frame = (self.frame + 1) % 8

        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        if self.x >= 800 or self.x <= 0:
            self.dir *= -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 40, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 40, 200, 200)


next_state = {
    SLEEP : {RU : RUN, LU : RUN, RD : RUN, LD : RUN},
    IDLE : {RU : RUN, LU : RUN, RD : RUN, LD : RUN, TIMER : SLEEP, KEY_A : AUTO_RUN},
    RUN  : {RU : IDLE, LU : IDLE, RD : IDLE, LD : IDLE, KEY_A : AUTO_RUN},
    AUTO_RUN  : {RU : AUTO_RUN, LU : AUTO_RUN, RD : RUN, LD : RUN, KEY_A : IDLE},
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.queue = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.queue:
            event = self.queue.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        
    
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def add_event(self, event):
        self.queue.insert(0, event)