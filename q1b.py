#!/usr/bin/env python
from numpy import arange
from math import pi, sin, cos
from utils import Window


def is_in_triangle(fa, fb, fc):
    e, f, g = sorted([fa, fb, fc])
    return e <= 0 and g >= 0


def rasterize_implicit(win, f):
    for px, py in win.pixels():
        x0, y0 = win.from_screen(px - 0.5, py - 0.5)
        x1, y1 = win.from_screen(px + 0.5, py + 0.5)
        fa = f(x0, y0)
        fb = f(x1, y0)
        fc = f(x1, y1)
        fd = f(x0, y1)
        if is_in_triangle(fa, fb, fc) or is_in_triangle(fa, fc, fd):
            win.pix[px, py] = 1


if __name__ == '__main__':
    win = Window(200, 200, (-1, 1), (-1, 1))
    rasterize_implicit(win, lambda x, y: x ** 2 + y ** 2 - 1)
    win.image.save("q1b.png")
