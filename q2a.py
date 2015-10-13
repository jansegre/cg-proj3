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
    win = Window(200, 200, (-100, 100), (-100, 100))
    #im = rasterize_parametric(win, lambda t: (t * sin(t), t * cos(t)), (0, 100), 0.1)
    rasterize_parametric(win, lambda t: (t * cos(t), t * sin(t)), (0, 100), 0.1)
    win.image.save("q2a.png")
