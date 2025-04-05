from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global marks
    reps = 0
    marks = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkmarks.config(text=marks)
    start_button.config(command=start_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if reps == 8:
        reset_timer()
    elif reps > 6:
       label.config(text="Break", fg=PINK)
       countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        label.config(text="Break", fg=GREEN)
        countdown(SHORT_BREAK_MIN * 60)
    else:
       label.config(text="Work", fg=RED)
       countdown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):# reps += 1
    # print(reps)
    global reps
    reset_button.config(command=reset_timer)
    start_button.config(command= "")
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
      global timer
      timer = window.after(1000, countdown, count - 1)
    else:
      global marks
      if reps % 2 == 0:
         marks += "✅"
         checkmarks.config(text=marks)
      reps += 1
      start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00",fill="white", font=(FONT_NAME,32, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME, 42))
label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmarks = Label( bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

window.mainloop()