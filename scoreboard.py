from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-25, 275)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", move=False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
