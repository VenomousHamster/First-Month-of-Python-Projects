from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from Food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.score_update()

    if snake.head.distance(food) < 15:
       scoreboard.score += 1
       snake.extend()
       food.refresh()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or  snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()