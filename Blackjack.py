import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



def user_cards():
      user_cards_selector = []
      dealer_cards = []

      user_cards_selector.append(random.choice(cards))
      user_cards_selector.append(random.choice(cards))
      dealer_cards.append(random.choice(cards))
      dealer_cards.append(random.choice(cards))
      player_score = sum(user_cards_selector)
      dealer_score = sum(dealer_cards)

      if player_score > 21 and cards[0] in user_cards_selector:
          location = user_cards_selector.index(11)
          user_cards_selector[location] = 1
          player_score = sum(user_cards_selector)


      hit_or_pass = 'y'

      while hit_or_pass == 'y':
            print(f"Your cards are: {user_cards_selector} your score is: {player_score}")
            print(f"The dealers face up card is: {dealer_cards[0]}")
            hit_or_pass = input("Do you want to hit or pass? 'y' to hit or 'n' to pass.\n").lower()

            if hit_or_pass == 'y':
               user_cards_selector.append(random.choice(cards))
               player_score = sum(user_cards_selector)
            if player_score > 21 and cards[0] in user_cards_selector:
                 location = user_cards_selector.index(11)
                 user_cards_selector[location] = 1
                 player_score = sum(user_cards_selector)

            if player_score > 21:
                hit_or_pass = "n"




      while dealer_score < 17 and player_score < 22:
         dealer_cards.append(random.choice(cards))
         dealer_score = sum(dealer_cards)

      if player_score > 21:
           print(f"Your cards are: {user_cards_selector} your score is: {player_score}")
           print("You went over. Dealer wins.")
      elif dealer_score > 21:
          print(f"Your cards are: {user_cards_selector} your score is: {player_score}")
          print(f"The dealers cards are: {dealer_cards} the dealers score: {dealer_score}")
          print("Dealer went over. You Win!")
      elif  player_score > dealer_score:
          print(f"Your cards are: {user_cards_selector} your score is: {player_score}")
          print(f"The dealers cards are: {dealer_cards} the dealers score: {dealer_score}")
          print("You Win!")
      else:
          print(f"Your cards are: {user_cards_selector} your score is: {player_score}")
          print(f"The dealers cards are: {dealer_cards} the dealers score: {dealer_score}")
          print("Dealer Wins.")




continue_game = True
while continue_game:
    print(logo)
    user_choice = input("Do you want play a round of blackjack? 'Y' for yes and 'N' for no.\n").lower()
    if user_choice == 'y':
        user_cards()
    elif user_choice == 'n':
        print("Goodbye!")
        continue_game = False
    else:
        print("Invalid choice try again.")

