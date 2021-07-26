import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
turns = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chance = random.randint(1,6)
    if random_chance == 1:
        car_manager.create_car()

    car_manager.move_cars()

    #Detect successful crossing
    if turtle.is_at_finishline():
        turtle.go_to_start()
        scoreboard.level_up()
        car_manager.increase_speed()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 25:
            game_is_on = False
            scoreboard.game_over()
    
screen.exitonclick()
    

    

