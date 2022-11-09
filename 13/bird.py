from pico2d import *
import random
import game_framework

#1 : 이벤트 정의
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 60.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

BIRD_IMAGE_WIDTH = 183 # PIXEL
BIRD_IMAGE_HEIGHT = 168 # PIXEL

BIRD_WIDTH = BIRD_IMAGE_WIDTH / 2
BIRD_HEIGHT = BIRD_IMAGE_HEIGHT / 2

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)
        if self.x <= 0 or self.x >= 1600:
            self.dir *= -1

    @staticmethod
    def draw(self):
        composite = ''
        if self.dir == -1:
            composite = 'h'
        self.image.clip_composite_draw(int(self.frame / 5) * BIRD_IMAGE_WIDTH, 0, BIRD_IMAGE_WIDTH, BIRD_IMAGE_HEIGHT, 0, composite, self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(450, 550)
        self.frame = 0
        self.dir = 1
        self.image = load_image('bird_animation.png')

        self.cur_state = IDLE
        self.cur_state.enter(self)
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)