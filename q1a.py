#!/usr/bin/env python
from numpy import arange
from math import pi, sin, cos
from utils import Window


def rasterize_parametric(win, f, (t0, tf), dt):
    for t in arange(t0, tf, dt):
        fx, fy = f(t)
        px, py = win.to_screen(fx, fy)
        if win.in_screen(px, py):
            win.pix[px, py] = 1


if __name__ == '__main__':
    win = Window(200, 200, (-1, 1), (-1, 1))
    rasterize_parametric(win, lambda t: (sin(t), cos(t)), (0, 2 * pi), 0.01)
    win.image.save("q1a.png")
