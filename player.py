from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("turtle")
         self.color("green")
         self.penup()
         self.setheading(90)
         self.goto(STARTING_POSITION)


     def go_up(self):
         self.forward(MOVE_DISTANCE)

     def move_right(self):
         new_x_position = self.xcor() + 10
         current_y_position = self.ycor()
         self.goto(new_x_position,current_y_position)

     def move_left(self):
         new_x_position = self.xcor() - 10
         current_y_position = self.ycor()
         self.goto(new_x_position, current_y_position)

     def is_at_finish_line(self):
         if self.ycor() > FINISH_LINE_Y:
             return True
         else:
             return False


     def reset_player(self):
         self.goto(STARTING_POSITION)


