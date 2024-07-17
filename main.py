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
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

canvas= Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="/Users/SAMEH/Desktop/web/python/pomodoro/tomato.png")
canvas.create_image(100 ,112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white" ,font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



window.mainloop()