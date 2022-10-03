from pico2d import *

os.chdir(os.path.dirname(__file__))
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir_vert, dir_hori, look_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                look_dir = 1
                dir_vert += 1
            elif event.key == SDLK_LEFT:
                look_dir = -1
                dir_vert -= 1
            elif event.key == SDLK_UP:
                dir_hori += 1
            elif event.key == SDLK_DOWN:
                dir_hori -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_vert -= 1
            elif event.key == SDLK_LEFT:
                dir_vert += 1
            elif event.key == SDLK_UP:
                dir_hori -= 1
            elif event.key == SDLK_DOWN:
                dir_hori += 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = KPU_WIDTH // 2
y = KPU_HEIGHT // 2
frame = 0
dir_hori = 0
dir_vert = 0
look_dir = 1

character_width = 100
character_height = 100
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if dir_vert == 0 and dir_hori == 0:
        if look_dir == 1:
            character.clip_draw(frame * 100, 100 * 3, character_width, character_height, x, y)
        elif look_dir == -1:
            character.clip_draw(frame * 100, 100 * 2, character_width, character_height, x, y)
    elif dir_vert == 1 or (dir_vert == 0 and look_dir == 1):
        character.clip_draw(frame * 100, 100 * 1, character_width, character_height, x, y)
    elif dir_vert == -1 or (dir_vert == 0 and look_dir == -1):
        character.clip_draw(frame * 100, 100 * 0, character_width, character_height, x, y)
    

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir_vert * 5
    y += dir_hori * 5

    box_width = 50
    box_height = 100

    left = x - box_width//2
    right = x + box_width//2
    top = y + box_width//2
    bottom = y - box_width//2
    if left < 0 or right > KPU_WIDTH:
        x -= dir_vert * 5
    if bottom < 0 or top > KPU_HEIGHT:
        y -= dir_hori * 5

    delay(0.01)

close_canvas()

