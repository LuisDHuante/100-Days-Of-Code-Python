from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.pensize(5)


def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def clockwise():
    turtle.right(10)


def counter_clockwise():
    turtle.left(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "c", fun = clear)



screen.exitonclick()