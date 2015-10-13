#!/usr/bin/env python
from numpy import arange
from math import pi, sin, cos
from utils import Window


def rasterize_implicit_region(win, f):
    for px, py in win.pixels():
        x0, y0 = win.from_screen(px - 0.5, py - 0.5)
        x1, y1 = win.from_screen(px + 0.5, py + 0.5)
        fa = f(x0, y0)
        fb = f(x1, y0)
        fc = f(x1, y1)
        fd = f(x0, y1)
        if any([fa, fb, fc, fd]):
            win.pix[px, py] = 1


if __name__ == '__main__':
    win = Window(200, 200, (0, 1), (0, 1))
    rasterize_implicit_region(win, lambda x, y: x + y > 1 and x ** 2 + (y - 1) ** 2 < 1 and (x - 1) ** 2 + y ** 2 < 1)
    win.image.save("q3.png")
