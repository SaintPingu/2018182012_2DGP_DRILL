from pico2d import *

class Sprite:
    def __init__(self, image, max_frame, origin, width, height):
        self.image : Image = image
        self.max_frame = max_frame
        self.origin = origin
        self.width = width
        self.height = height

        self.frame = 0
    
    def draw_frame(self, position, width=None, height=None):
        origin = self.origin[0] + (self.width * (self.frame % self.max_frame)), self.origin[1]
        self.image.clip_draw(*origin, self.width, self.height, *position, width, height)
        self.frame += 1

class Object:
    def __init__(self, position, width, height):
        self.position = position

        self.width = width
        self.height = height

        self.sprite = None

    def set_sprite(self, image : Image, max_frame, origin, width=None, height=None):
        if width == None:
            width = self.width
        if height == None:
            height = self.height
        
        origin = origin[0], image.h - origin[1]

        self.sprite = Sprite(image, max_frame, origin, width, height)

    def draw(self):
        if self.sprite:
            self.sprite.draw_frame(self.position, self.width, self.height)

os.chdir(os.path.dirname(__file__))

open_canvas()
sprite_sheet = load_image('sheet.png')

object_1 = Object((100,300), 90, 120)
object_1.set_sprite(sprite_sheet, 12, (0, 40), 33, 40)

object_2 = Object((300,300), 90, 120)
object_2.set_sprite(sprite_sheet, 12, (441, 40), 35, 40)

object_3 = Object((500,300), 140, 100)
object_3.set_sprite(sprite_sheet, 8, (0, 210), 69, 50)

object_4 = Object((700,300), 100, 90)
object_4.set_sprite(sprite_sheet, 15, (26, 535), 50, 46)

while True:
    clear_canvas()
    object_1.draw()
    object_2.draw()
    object_3.draw()
    object_4.draw()
    update_canvas()
    delay(0.1)

close_canvas()