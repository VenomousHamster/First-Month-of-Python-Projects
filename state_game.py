import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
correct_states = []

def check_answer(answer):
   data = pandas.read_csv("50_states.csv")
   for point in data["state"]:
     if answer not in correct_states and answer == point:
        correct_states.append(answer)
        return True
   return False


def state_on_map(correct_answer):
    data = pandas.read_csv("50_states.csv")
    temp_turtle = Turtle()
    temp_turtle.hideturtle()
    current_state = data[data.state == correct_answer]
    x_position = int(current_state.x.iloc[0])
    y_position = int(current_state.y.iloc[0])
    temp_turtle.teleport(x=x_position, y=y_position)
    temp_turtle.write(f"{correct_answer}", align="center", font=("Aria", 8, "normal"))


game_on = True
while game_on:
  answer_state = screen.textinput(title=f"{score}/50 states. Type 'exit' to give up.", prompt="What's another state's name?").title()
  state_data = pandas.read_csv("50_states.csv")
  is_right = check_answer(answer_state)
  if answer_state == "Exit":
    missed_states = [state for state in state_data["state"] if state not in correct_states]
    new_data = pandas.DataFrame(missed_states)
    new_data.to_csv("states_to_learn.csv")
    game_on = False

  if is_right:
      score += 1
      state_on_map(answer_state)

  if score == 50:
      turtle.write("Congrats! You named all fifty.", align="center", font=("Aria", 35, "normal"))
      game_on = False




