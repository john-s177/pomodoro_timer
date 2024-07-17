from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

canvas= Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="/Users/SAMEH/Desktop/web/python/pomodoro/tomato.png")
canvas.create_image(100 ,112, image=tomato)
canvas.create_text(103, 130, text="00:00", fill="white" ,font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()