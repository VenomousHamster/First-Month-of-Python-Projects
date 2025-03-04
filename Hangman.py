import random
import hangman_words
import hangman_art
word_list = hangman_words.word_list
lives = 6
stages = hangman_art.stages


chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(hangman_art.logo)
print("Word to guess: " + placeholder)
print(stages[lives])
game_over = False
correct_letters = []
player_chosen_characters = []

while not game_over:


    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in player_chosen_characters:
        print(f"You've guessed: {guess}. Before try again. ")


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word and guess not in player_chosen_characters:
        lives -= 1
        print(f"There is no {guess}. You lose a life.")

        if lives == 0:
            game_over = True


            print(f"***********************YOU LOSE**********************\n"
                  f"The word was {chosen_word}. ")

    player_chosen_characters.append(guess)

    if "_" not in display:
         game_over = True
         print("****************************YOU WIN****************************")


    print(stages[lives])