from turtle import Turtle

class Ball(Turtle):
   def __init__(self):
     super().__init__()
     self.shape("circle")
     self.color("white")
     self.penup()
     self.x_move = -10
     self.y_move =  10
     self.move_speed = 0.1

   def reset_ball(self):
       self.home()
       self.move_speed = 0.1
       self.bounce_x()


   def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(x=new_x, y=new_y)

   def bounce_y(self):
       self.y_move *= -1

   def bounce_x(self):
       self.x_move *= -1
       self.move_speed *= 0.8