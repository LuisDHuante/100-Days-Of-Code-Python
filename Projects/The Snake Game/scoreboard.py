from turtle import Turtle
import random


ALIGNMENT = "center"
FONT = ("Courier New", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align =  ALIGNMENT, font = FONT)


    def increase_score(self):
        self.score += 1
        self.show_score()
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.show_score()


    def title(self):
        self.goto(0, 0)
        self.write("The Snake Game\nClick to start", align =  ALIGNMENT, font = FONT)


