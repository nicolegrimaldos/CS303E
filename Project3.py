# File: Project3.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/29/2020
# Date Last Modified: 11/29/2020
# Description of Program: Create the American Flag using Turtle Graphics

import turtle


def drawStripes(ttl, x, y, length, width):
    ttl.penup()  #
    ttl.goto(x, y)  #
    ttl.setheading(0)
    for i in range(2):
        ttl.forward(length)  #
        ttl.right(90)
        ttl.forward(width)
        ttl.right(90)
    ttl.penup()


def colorFillStripes(ttl, x, y, length, width, fill):
    if fill:
        ttl.screen.colormode(255)
        ttl.fillcolor(191, 13, 62)
        ttl.fillcolor("red")
        ttl.begin_fill()
        y += width
        drawStripes(ttl, x, y, length, width)
        ttl.end_fill()
    else:
        ttl.fillcolor("white")
        ttl.begin_fill()
        y += width
        drawStripes(ttl, x, y, length, width)
        ttl.end_fill()


def colorBlueBox(ttl):
    ttl.screen.colormode(255)
    ttl.fillcolor(0, 32, 91)
    ttl.begin_fill()
    drawSquare(ttl)
    ttl.end_fill()


def drawSquare(ttl):
    ttl.penup()  #
    ttl.goto(-295, 79)  #
    ttl.setheading(0)
    ttl.pendown()
    for i in range(2):
        ttl.screen.colormode(255)
        ttl.pencolor(0, 32, 91)
        ttl.forward(210)  #
        ttl.right(90)
        ttl.forward(137)
        ttl.right(90)
    ttl.penup()


def drawStar(ttl, x, y, angle, size):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.pencolor("white")
    ttl.fillcolor("white")
    ttl.begin_fill()
    for i in range(5):
        ttl.pensize(1)
        ttl.forward(size)
        ttl.right(angle)
    ttl.end_fill()
    ttl.penup()
    ttl.goto(x + 3, y)
    ttl.pendown()
    ttl.pencolor("white")
    ttl.fillcolor("white")
    ttl.begin_fill()
    for i in range(5):
        ttl.forward(2)
        ttl.right(72)
    ttl.end_fill()
    ttl.penup()


def starRow(ttl):
    x = -283
    y = 70
    for i in range(4):
        for t in range(6):
            drawStar(ttl, x, y, 144, 10)
            x += 35
        x = -265
        y -= 14
        for n in range(5):
            drawStar(ttl, x, y, 144, 10)
            x += 35
        x = -283
        y -= 14
    for t in range(6):
        drawStar(ttl, x, y, 144, 10)
        x += 35


def AmericanFlag(ttl, x, y, length, width):
    fill = True
    for i in range(14):
        y += width
        colorFillStripes(ttl, x, y, length, width, fill)
        fill = not fill
    colorBlueBox(ttl)
    starRow(ttl)


Bob = turtle.Turtle()
Bob.speed(150)
Bob.pensize(3)
AmericanFlag(Bob, -295, -200, 490, 20)

turtle.done()
