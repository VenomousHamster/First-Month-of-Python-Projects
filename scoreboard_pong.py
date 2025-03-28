from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.left_winner = "Congrats you won!"
        self.right_winner = "Sorry you lost."

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-110, y=220)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(110, 220)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def player_win(self):
      self.goto(0, 0)
      self.write(self.left_winner, align="center", font=("Courier", 30, "normal"))

    def player_loss(self):
        self.goto(0, 0)
        self.write(self.right_winner, align="center", font=("Courier", 30, "normal"))
