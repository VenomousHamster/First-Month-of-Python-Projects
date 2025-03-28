from turtle import Turtle
import random

DISTANCE = 25


class Paddle(Turtle):

    def __init__(self, position):
       super().__init__()
       self.shape("square")
       self.penup()
       self.color("white")
       self.turtlesize(stretch_wid=1, stretch_len=5)
       self.setheading(90)
       self.goto(position)


    def up(self):
      self.forward(DISTANCE)

    def down(self):
      self.backward(DISTANCE)


    def cpu_move_forward(self):
        self.forward(30)


    def rotate_cpu_down(self):
        self.setheading(270)

    def rotate_cpu_up(self):
        self.setheading(-270)