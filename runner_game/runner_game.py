import pgzrun
import pygame as pg
from random import randint
from time import time

TITLE = "Runner Game"
WIDTH = 1100
HEIGHT = 550

jump_pressed = False

warrior = Actor("warrior")
warrior.pos = (randint(70,WIDTH-70),378)

def draw():
    screen.blit("background",(0,0))
    warrior.draw()
    
def update():
    global jump_pressed
    if keyboard.left:
        warrior.x -= 3
    if keyboard.right:
        warrior.x += 3
    if jump_pressed == False:
        if keyboard.up:
            jump_pressed = True
            if jump_pressed:
                start_time = time()
                warrior.y -= 10 + round(time()-start_time)*4
                jump_pressed = False
    


pgzrun.go()