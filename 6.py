from turtle import *
tracer(0)
left(90)

k = 10
for i in range(10):
    goto(20 * k, 10 * k)
    goto(-5 * k, -15 * k)
    goto(-15 * k, 5 * k)

up()
for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x * k, y * k)
        dot(4)

done()