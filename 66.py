from turtle import *
k = 20
left(90)
speed(100000)
x, y = xcor(), ycor()

for i in range(10):
    x += 200
    y += 100
    goto(x, y)
    x += -50
    y += -150
    goto(x, y)
    x += -150
    y += 50
    goto(x, y)

done()