from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-225, 250)
        self.write(f"Level: {self.score}", align="center",
                   font=("Courier", 15, "normal"))


    def add_point(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 20, "normal"))



