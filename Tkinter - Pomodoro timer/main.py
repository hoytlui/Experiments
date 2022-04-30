import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BEIGE = "#fdf6ec"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # reset time
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')

    # reset title
    title_label.config(text="Timer")
    
    # reset checkmark
    checkmark.config(text="")

    # reset repetitions
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # work -> sb -> work -> sb -> work -> sb -> work -> lb
    if reps % 2 != 0:
        countdown(work_sec)
        title_label.config(text="Work", fg=PINK)
    elif reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=GREEN)
    else:
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # convert min into min and sec
    count_min = count // 60
    count_sec = count % 60

    # display text
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")  # string formatting
    
    # iterate own function
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)  # await certain time (in ms) before calling function
    else:
        start_timer()

        # record repetitions
        tick = ""
        work_session = reps // 2
        for _ in range(work_session):
            tick += "✓"
        checkmark.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
# set up window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=BEIGE)


# create canvas
canvas = tk.Canvas(width=210, height=230, bg=BEIGE, highlightthickness=0)
# add image
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)
# add text
timer_text = canvas.create_text(113, 138, text='00:00', fill='lightpink', font=(FONT_NAME, 36, 'bold'))

# create title
title_label = tk.Label(text="Timer", fg=GREEN, bg=BEIGE, font=(FONT_NAME, 48, 'bold'))

# create buttons
start_button = tk.Button(text="Start", highlightbackground=BEIGE, command=start_timer)
reset_button = tk.Button(text="Reset", highlightbackground=BEIGE, command=reset_timer)

# create tick
checkmark = tk.Label(text="", fg=GREEN, bg=BEIGE, font=(FONT_NAME, 28))

# position
title_label.grid(row=1, column=2)
canvas.grid(row=2, column=2)
start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)
checkmark.grid(row=4, column=2)

# loop until closed
window.mainloop()