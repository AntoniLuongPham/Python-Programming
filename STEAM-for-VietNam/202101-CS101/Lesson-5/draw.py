from turtle import *
penup()
goto(-100, 100)
pendown()
i2 = 0
i = 0
while i2 < 4:
    while i < 5:
        forward(110)
        right(70)
        i += 1
    forward(90)
    i = 0
    while i < 5:
        forward(110)
        right(70)
        i += 1
    forward(90)
    i2 += 1
i2 = 0
while i2 < 4:
    while i < 5:
        backward(110)
        right(70)
        i += 1
    backward(90)
    i = 0
    while i < 5:
        backward(110)
        right(70)
        i += 1
    backward(90)
    i2 += 1
