#Challenge 3:
from turtle import Turtle, Screen
from random import choice


turtle = Turtle()
colors = ["medium blue", "dark slate gray","red","dark orange","dark magenta","maroon","green","black"]
turtle.pensize(width=5)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(50)
        turtle.right(angle)


for i in range(3,11):
    turtle.pencolor(choice(colors)) 
    draw_shape(i)



# """Triangle"""
# for _ in range(3):
#     turtle.pencolor("brown")
#     turtle.forward(50)
#     turtle.right(120)

# """Square"""
# for _ in range(4):
#     turtle.pencolor("pink")
#     turtle.forward(50)
#     turtle.right(90)

# """"Pentagon """
# for _ in range(5):
#     turtle.pencolor("black")
#     turtle.forward(50)
#     turtle.right(72)

# """Hexagon"""
# for _ in range(6):
#     turtle.pencolor("purple")
#     turtle.forward(50)
#     turtle.right(60)


# """Heptagon"""
# for _ in range(7):
#     turtle.pencolor("yellow")
#     turtle.forward(50)
#     turtle.right(51.43)


# """Octagon"""
# for _ in range(8):
#     turtle.pencolor("red")
#     turtle.forward(50)
#     turtle.right(45)


# """Nonagon"""
# for _ in range(9):
#     turtle.pencolor("green")
#     turtle.forward(50)
#     turtle.right(40)


# """Decagon"""
# for _ in range(10):
#     turtle.pencolor("blue")
#     turtle.forward(50)
#     turtle.right(36)


screen = Screen()
screen.exitonclick()