import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from frogger_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkey(turtle.go_up, "w")
screen.onkey(turtle.move_left, "a")
screen.onkey(turtle.move_right, "d")


car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()

    if turtle.is_at_finish_line():
        turtle.reset_player()
        car_manager.speed_increase()
        scoreboard.new_level()

    for car in car_manager.list_of_cars:
        if car.distance(turtle) < 20:
           scoreboard.game_over()
           game_is_on = False

    car_manager.move_cars()


screen.exitonclick()