import random

logo = r'''
 __      __       .__                                  __             __  .__                                                       
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|  |__   ____                                             
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |  \_/ __ \                                            
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |   Y  \  ___/                                            
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |___|  /\___  >                                           
       \/       \/          \/            \/     \/                            \/     \/                                            
                    ___.                                                      .__                                                   
  ____  __ __  _____\_ |__   ___________     ____  __ __   ____   ______ _____|__| ____    ____      _________    _____   ____      
 /    \|  |  \/     \| __ \_/ __ \_  __ \   / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \     
|   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/  / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/     
|___|  /____/|__|_|  /___  /\___  >__|     \___  /|____/  \___  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  > /\ 
     \/            \/    \/     \/        /_____/             \/     \/     \/        \//_____/   /_____/     \/      \/     \/  \/ 
'''
print(logo)
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1,100)
lives = 0

difficulty = input("Choose a difficulty. Typer 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
else:
    lives = 5

game_over = False
user_guess = 0

while not game_over:
    print(f"You have {lives} attempts left to guess the number.")
    user_guess = int(input(f"Make a guess: "))
    if user_guess < random_number:
        print("Too Low!")
        lives -= 1
    elif user_guess > random_number:
        lives -= 1
        print("Too High!")
    elif user_guess == random_number:
        game_over = True
        print(f"You got it! The answer was {random_number}.")
    if lives == 0:
        game_over = True
        print(f"Game Over! The answer was: {random_number}. ")




