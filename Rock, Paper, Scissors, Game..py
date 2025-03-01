import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = ["Rock","Paper","Scissors"]

pictures = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
print("You chose:")
print(pictures[player_choice])

computer_choice = random.choice(rock_paper_scissors)
print("Computer chose:")

if  player_choice >= 3 or player_choice < 0:
    print("Invalid number you lose.")

if player_choice == 0:
    if computer_choice == "Rock":
        print(rock)
        print("Draw.")
    if computer_choice == "Paper":
        print(paper)
        print("You lose.")
    if computer_choice == "Scissors":
        print(scissors)
        print("You win!")

if player_choice == 1:
    if computer_choice == "Rock":
        print(rock)
        print("You win!")
    if computer_choice == "Paper":
        print(paper)
        print("Draw.")
    if computer_choice == "Scissors":
        print(scissors)
        print("Lose!")

if player_choice == 2:
    if computer_choice == "Rock":
        print(rock)
        print("You lose!")
    if computer_choice == "Paper":
        print(paper)
        print("You win!")
    if computer_choice == "Scissors":
       print(scissors)
       print("Draw.")
