import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {nato.letter[index]:code.code for (index,code) in nato.iterrows()}
user_word = [char for char in input("Pleas enter a word: ").upper()]
code_list = [alphabet[i] for i in user_word]
print(code_list)
