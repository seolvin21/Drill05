import random
import math
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

cursor = load_image('hand_arrow.png')
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def character_move(cx, cy):
    global x, y, i
    global arrive

    t = i / 100
    x = (1 - t) * x + t * cx
    y = (1 - t) * y + t * cy

    if i > 100:
        i = 0
        arrive = True
    else:
        i = i + 1


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


arrive, running = False, True
x, y = 0, 0
cx, cy = random.randint(-400, 400), random.randint(-400, 400)
i = 100
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if arrive:
        arrive = False
        cx, cy = random.randint(0, 1280), random.randint(0, 1024)
        i = 0

    character_move(cx, cy)

    # if character_left:
    #     character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, x, y)
    # elif character_right:
    #     character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    cursor.clip_draw(0, 0, 50, 52, cx, cy)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    frame = (frame + 1) % 8


    handle_events()
    update_canvas()

    delay(0.01)

close_canvas()