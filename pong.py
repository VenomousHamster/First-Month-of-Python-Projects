from turtle import Screen
from paddle import Paddle
from ball   import Ball
from scoreboard_pong import Scoreboard
import time

PLAYER_POSITION = (-370,0)
CPU_POSITION = (370,-280)
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(PLAYER_POSITION)
r_paddle = Paddle(CPU_POSITION)
ball = Ball()
screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
# screen.onkey(r_paddle.up,  "Up")
# screen.onkey(r_paddle.down, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    if r_paddle.ycor() < 260:
       r_paddle.cpu_move_forward()

    if r_paddle.ycor() >= 260:
        r_paddle.rotate_cpu_down()
        r_paddle.cpu_move_forward()

    if r_paddle.ycor() <= -260:
        r_paddle.rotate_cpu_up()
        r_paddle.cpu_move_forward()

    # top and bottom collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #paddle collision detection
    if ball.distance(l_paddle) < 30 and ball.xcor() < -340 or ball.distance(r_paddle) < 30 and ball.xcor() > 340:
        ball.bounce_x()

    # right side detection.
    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.l_point()

    # left side detection.
    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_point()

    if scoreboard.l_score == 5:
        scoreboard.player_win()
        is_game_on = False

    if scoreboard.r_score == 5:
        scoreboard.player_loss()
        is_game_on = False


screen.exitonclick()