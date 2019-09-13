#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    CTIM-285 W01 / Professor Janet Brown-Sederberg
    04 April 2019

    version 1.0: initial release
    version 1.1: add random colors to the initials for fun, use functions
"""
import turtle
import random

def draw_k(x, y, color):
    k = turtle.Turtle()
    k.color(color)
    k.begin_fill()
    k.penup()
    k.goto(x,y)
    k.pendown()
    k.left(90)
    k.forward(280)
    k.circle(-20,180)
    k.forward(75)
    k.circle(10,90)
    k.left(45)
    k.forward(150)
    k.circle(-20,185)
    k.forward(150)
    k.circle(10,90)
    k.forward(160)
    k.circle(-20,180)
    k.forward(130)
    k.circle(10,120)
    k.left(20)
    k.forward(113)
    k.left(-20)
    k.circle(-20,180)
    k.goto(x,y)
    k.end_fill()
    k.hideturtle()

def draw_m(x, y, color):
    m = turtle.Turtle()
    m.penup()
    m.color(color)
    m.begin_fill()
    m.goto(x,y)
    m.left(90)
    m.pendown()
    m.forward(280)
    m.circle(-10,165)
    m.forward(240)
    m.circle(10,145)
    m.forward(240)
    m.circle(-10,160)
    m.forward(280)
    m.circle(-10,180)
    m.forward(200)
    m.circle(6,160)
    m.forward(190)
    m.circle(-16,145)
    m.forward(165)
    m.circle(10,165)
    m.forward(180)
    m.circle(-6,180)
    m.goto(x,y)
    m.end_fill()
    m.hideturtle()

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# main program
draw_k(-320, -40, random_color())
draw_m(-100, -40, random_color())
draw_m(128, -40, random_color())
turtle.done()
