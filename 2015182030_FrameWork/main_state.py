import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player
import Monster_Green
import ObjectMgr

name = "MainState"

m_ObjectMgr = None
m_map = None
font = None
reCreateTime=0

class Font:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)

class Map:
    def __init__(self):
        self.image = load_image('Tengai/Resource/Map/forest.png')

    def draw(self):
        self.image.draw(400, 300)


def enter():
    global  m_map,m_ObjectMgr

    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_ObjectMgr.Add_Object('PLAYER')
    m_ObjectMgr.Add_Object('MON_GREEN', None, 500, 100)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 500, 300)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 500, 500)

    m_map = Map()

def exit():
    global m_map,m_ObjectMgr
    del(m_map)
    m_ObjectMgr.Release_Object()

def pause():
    pass

def resume():
    pass

def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           game_framework.change_state(title_state)
       elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
           pass


def update():
    global  reCreateTime,m_ObjectMgr

    reCreateTime+=1
    if reCreateTime >= 100:
        print('Create Mon')
        reCreateTime=0
        for mon in range(3):
            m_ObjectMgr.Add_Object('MON_GREEN', None, 700, 100)
            m_ObjectMgr.Add_Object('MON_GREEN', None, 700, 300)
            m_ObjectMgr.Add_Object('MON_GREEN', None, 700, 500)

    m_ObjectMgr.Update_Object()

    delay(0.015)

def draw():
    clear_canvas()
    m_map.draw()
    m_ObjectMgr.Render_Object()
    update_canvas()

