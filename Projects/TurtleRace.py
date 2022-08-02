from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
colors = ["blue", "yellow", "red", "purple","pink", "green"]
y_positions = [-150, -100, -50, 0, 50, 100]
turtle_list = []

for i in range(0,6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -225, y = y_positions[i])
    turtle_list.append(new_turtle)


user_bet = screen.textinput(title= "Make your bet", prompt = "Which turtle will win the race?").lower()

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color was {winning_color}!")
            else:
                print(f"You've lost, the winning color was {winning_color}!")
        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)


screen.exitonclick()