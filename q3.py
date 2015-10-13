#!/usr/bin/env python
from numpy import arange
from math import pi, sin, cos
from utils import Window


def rasterize_implicit_region(win, f):
    for px, py in win.pixels():
        x, y = win.from_screen(px, py)
        if f(x, y):
            win.pix[px, py] = 1


if __name__ == '__main__':
    win = Window(200, 200, (0, 1), (0, 1))
    rasterize_implicit_region(win, lambda x, y: x + y > 1 and x ** 2 + (y - 1) ** 2 <= 1 and (x - 1) ** 2 + y ** 2 <= 1)
    win.image.save("q3.png")
