from pico2d import *
import math

def DrawScene():
    global character, grass
    global posX, posY
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(posX,posY)
    delay(0.01)

def MoveSquare():
    global moveAmount, posX, posY
    maxWidth = 800
    maxHeight = 600
    
    while posX <= (maxWidth - 20):
        posX += moveAmount
        DrawScene()
    posX = maxWidth - 20
    while posY <= (maxHeight - 60):
        posY += moveAmount
        DrawScene()
    posY = maxHeight - 60
    while posX > 30:
        posX -= moveAmount
        DrawScene()
    posX = 30
    while posY > 90:
        posY -= moveAmount
        DrawScene()
    posY = 90
    while posX < 400:
        posX += moveAmount
        DrawScene()
    posX = 400
def MoveCircle():
    global posX, posY
    radius = 230
    degree = 180
    while degree < (180 + 360):
        degree += 5
        rad = math.radians(degree)
        posX = 400 + (radius * math.sin(rad))
        posY = 330 + (radius * math.cos(rad))
        DrawScene()
    pass

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

moveAmount = 10
posX = 400
posY = 90

DrawScene()

while True:
    MoveSquare()
    MoveCircle()

close_canvas()