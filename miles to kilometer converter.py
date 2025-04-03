from tkinter import *

def converter():
   number = float(user_num.get()) * 1.60934
   km_num_display.config(text=f"is equal to {round(number,2)} Km.")

window = Tk()
window.title("Miles to Kilometer.")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

label = Label(text="Miles")
label.grid(column=2,row=0)

user_num = Entry(width=15)
user_num.grid(column=1,row=0)
user_num.focus()


cal_button = Button(text="Calculator", command=converter)
cal_button.grid(column=1,row=2)

km_num_display = Label(text=f" is equal to 0 Km.")
km_num_display.grid(column=1,row=1)


window.mainloop()