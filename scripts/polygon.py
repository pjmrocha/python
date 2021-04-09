#!/usr/bin/python

import turtle

def draw_poly(sides, size, color):
    angle = 360 / sides
    turtle.color(color)
    for n in range(sides):
        turtle.fd(size)
        turtle.lt(angle)

draw_poly(4, 100, "blue")

draw_poly(3, 150, "red")

draw_poly(6, 180, "green")
