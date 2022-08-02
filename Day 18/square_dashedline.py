from turtle import Screen, Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red", "blue2")

# Challenge 1: Square
for _ in range(4):
    turtle.forward(50)
    turtle.right(90)


# Challenge 2: Dashed Line
for _ in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


screen = Screen()
screen.exitonclick()