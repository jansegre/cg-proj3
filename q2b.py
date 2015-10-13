#!/usr/bin/env python
from numpy import arange
from math import pi, sin, cos
from utils import Window


def rasterize_parametric_adapt(win, f, (t0, tf), dt):
    t = tf
    while t > t0:
        fx, fy = f(t)
        px, py = win.to_screen(fx, fy)
        if win.in_screen(px, py):
            win.pix[px, py] = 1
        t = t - dt(t)


if __name__ == '__main__':
    win = Window(200, 200, (-100, 100), (-100, 100))
    #im = rasterize_parametric_adapt(win, lambda t: (t * sin(t), t * cos(t)), (0, 100), lambda t: 1.0 / t ** 2)
    rasterize_parametric_adapt(win, lambda t: (t * cos(t), t * sin(t)), (0, 100), lambda t: 1.0 / t ** 2)
    win.image.save("q2b.png")
