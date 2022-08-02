#Challenge 5: Spirograph
import turtle as t
import random


turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


for _ in range(100):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.forward(1)
    turtle.rt(99)


