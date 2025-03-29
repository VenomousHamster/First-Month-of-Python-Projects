import turtle
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

      def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

      def new_level(self):
          self.clear()
          self.level += 1
          self.write(f"Level: {self.level}", align="center", font=FONT)

      def game_over(self):
          self.goto(0,0)
          self.write(f"GAME OVER!", align="center", font=FONT)

