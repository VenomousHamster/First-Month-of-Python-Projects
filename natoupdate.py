import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {nato.letter[index]:code.code for (index,code) in nato.iterrows()}

def generate_code():
   user_word = [char for char in input("Pleas enter a word: ").upper()]
   try:
     code_list = [alphabet[i] for i in user_word]
   except KeyError:
       print("Sorry, no numbers.")
       generate_code()
   else:
      print(code_list)


generate_code()
