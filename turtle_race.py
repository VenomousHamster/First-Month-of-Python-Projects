from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_location = -90
is_race_on = False
all_turtles = []

user_bet = int(screen.textinput(title="Make your bet." , prompt="How much money do you want to bet? Enter: "))
user_choice = screen.textinput(title="Make your bet." , prompt="Which turtle will win the race? Enter a color: Red, Purple, Blue, Yellow, Green, or Orange: ").lower()

for i in range (0, 6):
    a_turtle = Turtle(shape="turtle")
    a_turtle.penup()
    a_turtle.color(colors[i])
    a_turtle.goto(x=-225, y=y_location)
    y_location += 40
    all_turtles.append(a_turtle)


if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
       if turtle.xcor() > 230:
           is_race_on = False
           winning_color = turtle.pencolor()
           if winning_color == user_choice:
               prize_money = user_bet * 2
               print(f"You have won! The {winning_color} is the winner! Your prize is: ${prize_money}")
           else:
               print(f"You have loss. The {winning_color} is the winner.")

       rand_distance = random.randint(0,10)
       turtle.forward(rand_distance)



screen.exitonclick()

