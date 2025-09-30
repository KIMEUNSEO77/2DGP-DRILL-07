from pico2d import *
import random

class Ball:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 599
        self.small_image = load_image('ball21x21.png')
        self.big_image = load_image('ball41x41.png')

open_canvas()

close_canvas()