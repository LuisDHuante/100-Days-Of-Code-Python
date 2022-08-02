#Final Project
import turtle as t
import random


colors = [(210, 149, 87), (33, 98, 150), (210, 211, 109), (129, 171, 202), (159, 58, 87), (169, 73, 41), (59, 123, 63), (209, 81, 106), (125, 185, 153), (221, 86, 56), (183, 150, 44), (10, 48, 92), (135, 35, 47), (197, 128, 159), (208, 215, 11), (72, 45, 32), (36, 62, 42), (25, 60, 123), (122, 41, 34),(25, 169, 141), (19, 91, 49), (152, 206, 213), (31, 176, 185), (155, 207, 191), (83, 77, 36), (221, 174, 186)]


turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()
t.colormode(255)
turtle.speed("fastest")
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(colors))
    turtle.forward(50)


    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()