from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
langauge_dict = {}
current_card = {}
learned_cards = {}
TIME = 1000 * 3

try:
    df = pd.read_csv("Words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = df.to_dict(orient="records")

def known_cards():
  global learned_cards
  learned_cards.update(current_card)
  language_dict.remove(current_card)
  data = pd.DataFrame(language_dict)
  data.to_csv("Words.csv", index=False)
  next_card()

def next_card():
    global current_card
    current_card = rd.choice(language_dict)
    x_button.config(command=NONE)
    cross_button.config(command=NONE)

    canvas.itemconfig(flash_card,image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    window.after(TIME, flip_card)

def flip_card():
     global current_card
     canvas.itemconfig(flash_card, image=card_back_img)
     canvas.itemconfig(title,text="English", fill="white")
     canvas.itemconfig(word,text=current_card["English"], fill="white")
     x_button.config(command=next_card)
     cross_button.config(command=known_cards)

window = Tk()
window.title("Flashcards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)




card_front_img = PhotoImage(file="card_front.png")
card_back_img =  PhotoImage(file="card_back.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

flash_card = canvas.create_image(400,263, image=card_front_img)
title = canvas.create_text(380,70, text="", font=("Ariel",30, "italic"))
word = canvas.create_text(380,263, text="", font=("Ariel",60, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_button = Button(image=right_img, width=95, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, highlightthickness=0, command=known_cards)
cross_button.grid(padx=200,column=1,row=1)

x_button = Button(image=wrong_img,bg=BACKGROUND_COLOR,fg="white", highlightthickness=0)
x_button.grid(padx=200, column=0,row=1)

next_card()

mainloop()
