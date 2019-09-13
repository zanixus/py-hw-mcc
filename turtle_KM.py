#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    CTIM-285 W01 / Professor Janet Brown-Sederberg
    02 Feb 2019

    This is an ugly Python script that calls the turtle library
    and prints the initials "KMM" the the screen with nice RGB colors.
    The curves of the letters are rounded.
    I have created functions to draw letters to avoid redundant code
    (although I did not avoid it too well as it's just a bunch of x, y
    and string arguments)

    version 1.0: initial release
"""
import turtle

def draw_k(x, y, color):
    k = turtle.Turtle()
    k.color(color)
    k.begin_fill()
    k.penup()
    #goto statements considered harmful
    k.goto(x,y)
    #but not to turtlekind
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

# main program
draw_k(-320, -40, "red")
draw_m(-100, -40, "green")
draw_m(128, -40, "blue")
turtle.done()
