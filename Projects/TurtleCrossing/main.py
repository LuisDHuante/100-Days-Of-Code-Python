import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Creating the cars
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect turtle collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect turtle reaching the other side
    if player.ycor() > 280:
        player.return_home()
        car_manager.level_up()
        scoreboard.add_point()




screen.exitonclick()
