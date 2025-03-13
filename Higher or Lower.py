from game_data import data
import random

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

person_a = random.choice(data)
person_b = random.choice(data)
print("Guess higher or lower instagram followers. If they are tied, you win. See how high of a score you can get.\n")
print(person_a)
print(person_b)

def compare_followers(a,b):
    print("\n"*200)
    print(logo)
    print(f"Your score: {score}.")
    print(f"Compare A: {person_a["name"]}, {person_a["description"]}, from {person_a["country"]}. ")
    print(vs)
    print(f"Compare B: {person_b["name"]}, {person_b["description"]}, from {person_b["country"]}. ")
    choice = input("Choose a or b.\n")
    print(choice)
    if a["follower_count"] > b["follower_count"] and choice == "a":
        return "right"
    elif b["follower_count"] > a["follower_count"] and choice == "b":
        return "right"
    elif a["follower_count"] == b["follower_count"]:
         print("It's a draw. So, that means.")
         return "draw"
    else:
        return "wrong"


def was_player_correct (answer):
    points = 0
    if answer == "wrong":
        print("You loss.")
        print("It's okay, you can go watch some hentai. ")
        return points
    else:
        print("You are right!")
        points += 1
        return points

#Hello, um. This isn't Hentai.
game_over = False
score = 0
last_score = 0

def grade():
    if score >= 5:
        print(f"Wow! Your score is: {score} That is amazing!")
    elif score >= 2:
        print(f"You scored: {score} not bad.")
    elif score > 0:
        print(f"You scored: {score} Well, at least you got one right.")
    else:
        print(f"score: {score} Wow! That was fast. It's okay. Everyone has something they can do for you it's watching hentai.")



while not game_over:
    abc = compare_followers(person_a, person_b)
    person_a = person_b
    score += was_player_correct(abc)
    if score == last_score:
        grade()
        game_over = True
    if person_a == person_b:
        person_b = random.choice(data)
    last_score = score

