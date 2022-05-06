import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = '#204231'

# create idiom dict
idiom_df = pd.read_csv('data/idioms.csv')
idiom_dict = idiom_df.to_dict(orient='records')
current_card_dict = {}


# -------------------- GO TO NEXT CARD -------------------- #
def next_card():
    global current_card_dict, flip_timer
    # start flip timer
    window.after_cancel(flip_timer)
    # select idiom
    current_card_dict = random.choice(idiom_dict)
    # set appearance of card
    canvas.itemconfig(title_text, text='Idiom', fill=FONT_COLOR)
    canvas.itemconfig(meaning_text, text=current_card_dict['Idiom'], fill=FONT_COLOR)
    canvas.itemconfig(card_background, image=card_front_img)
    # reset flip timer and call flip_card function
    flip_timer = window.after(3000, func=flip_card)


# -------------------- GO TO THE BACK OF THE CARD -------------------- #
def flip_card():
    # change appearance of card
    canvas.itemconfig(title_text, text='Meaning', fill=FONT_COLOR)
    canvas.itemconfig(meaning_text, text=current_card_dict['Meaning'], fill=FONT_COLOR)
    canvas.itemconfig(card_background, image=card_back_img)


# -------------------- REMOVE IDIOM FROM DICT -------------------- #
def got_it():
    # remove idiom from dict
    idiom_dict.remove(current_card_dict)
    next_card()


# -------------------- UI SETUP -------------------- #
# set up window
window = tk.Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# flip card after certain time
flip_timer = window.after(3000, func=flip_card)

# create canvas
canvas = tk.Canvas(width=800, height=526)
# add image
card_front_img = tk.PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = tk.PhotoImage(file='images/card_back.png')
# add text
title_text = canvas.create_text(400, 120, text='', font=('Ariel', 36, 'italic'))
meaning_text = canvas.create_text(400, 280, text='', font=('Ariel', 48, 'bold'), width=720)

# create button
cross_img = tk.PhotoImage(file='images/wrong.png')
cross_button = tk.Button(image=cross_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
tick_img = tk.PhotoImage(file='images/right.png')
tick_button = tk.Button(image=tick_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=got_it)

# position
canvas.grid(row=1, column=1, columnspan=2)
cross_button.grid(row=2, column=1)
tick_button.grid(row=2, column=2)

# call next_card function to show current card
next_card()

window.mainloop()