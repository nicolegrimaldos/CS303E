# File: GermanFlag.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/21/2020
# Date Last Modified: 11/26/2020
# Description of Program: Create the German Flag using Turtle Graphics

import turtle


def drawSquare(ttl, x, y, length, width):
    ttl.penup()  #
    ttl.goto(x, y)  #
    ttl.setheading(0)
    ttl.pendown()
    for i in range(2):
        ttl.forward(length)  #
        ttl.right(90)
        ttl.forward(width)
        ttl.right(90)
    ttl.penup()


def colorFillSquare(ttl, x, y, length, width, color):
    if color == "yellow":
        ttl.screen.colormode(255)
        ttl.fillcolor(255, 205, 0)
        ttl.begin_fill()
        drawSquare(ttl, x, y, length, width)
        ttl.end_fill()
    elif color == "red":
        ttl.screen.colormode(255)
        ttl.fillcolor(218, 41, 28)
        ttl.begin_fill()
        drawSquare(ttl, x, y, length, width)
        ttl.end_fill()
    else:
        ttl.fillcolor(color)
        ttl.begin_fill()
        drawSquare(ttl, x, y, length, width)
        ttl.end_fill()


def GermanFlag(ttl, x, y, length, width):
    n = 1
    while n < 4:
        if n == 1:
            ttl.screen.colormode(255)
            ttl.pencolor(255, 205, 0)
            color = "yellow"
            colorFillSquare(ttl, x, y, length, width, color)
            n += 1
        elif n == 2:
            ttl.screen.colormode(255)
            ttl.pencolor(218, 41, 28)
            color = "red"
            y += width
            colorFillSquare(ttl, x, y, length, width, color)
            n += 1
        else:
            ttl.pencolor('black')
            color = "black"
            y += width
            colorFillSquare(ttl, x, y, length, width, color)
            n += 1


Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)
GermanFlag(Bob, -300, 0, 500, 100)

turtle.done()
