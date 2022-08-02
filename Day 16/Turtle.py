#Importing variables from other files
# import module

# print(module.variable)

#Importing Turtle
from turtle import Turtle, Screen

turtle = Turtle()
print(turtle)
turtle.shape("turtle")
turtle.color("blue", "red")
my_screen = Screen()
turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

