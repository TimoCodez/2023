# ----------------------------- IMPORTS ----------------------------------#
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
TEST = "Program closed successfully"
REPS = 0
TIMER = None
IS_TIMER_RUNNING = False

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global IS_TIMER_RUNNING
    IS_TIMER_RUNNING = False
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global IS_TIMER_RUNNING
    if IS_TIMER_RUNNING:
        return
    IS_TIMER_RUNNING = True
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Grind!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Python Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=300, height=300, bg="YELLOW", highlightthickness=0)
tomato_img = PhotoImage(file="tomato2.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 70, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Begin", padx=5, pady=5, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", padx=5, pady=5, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)


window.mainloop()
print(TEST)
