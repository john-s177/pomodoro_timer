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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00") 
    title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count/60)
    count_sec = count % 60
    if count_sec in range(0,10):
        count_sec="0"+str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_sessions=int(reps/2)
        for _ in range (work_sessions):
            marks+="✓"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label( fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

canvas= Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="/Users/SAMEH/Desktop/web/python/pomodoro/tomato.png")
canvas.create_image(100 ,112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white" ,font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



window.mainloop()