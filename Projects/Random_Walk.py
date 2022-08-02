#Challenge 4:
import turtle as t
import random


turtle = t.Turtle()
t.colormode(255)
turtle.pensize(5)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


movements = [0, 90, 180, 270]


turtle.speed("fastest")


for _ in range(2000):
    turtle.color(random_color())
    turtle.forward(20)
    turtle.setheading(random.choice(movements))


screen = t.Screen()
screen.exitonclick()

    
    
