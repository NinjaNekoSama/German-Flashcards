from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/german_words.csv")

my_dict = data.to_dict(orient='records')
word = {}


# ---------------------------- SAVE CARDS ------------------------------- #

def randomize_right_cards():
    my_dict.remove(word)
    print(len(my_dict))
    words_to_learn = pandas.DataFrame(my_dict)
    words_to_learn.to_csv("words_to_learn.csv", index=False)
    randomize_wrong_cards()


# ---------------------------- NEW CARDS ------------------------------- #


def randomize_wrong_cards():
    global word
    word = my_dict[random.randint(0, len(my_dict) - 1)]

    canvas.itemconfig(word_old, text=f"{word['German']}", fill="black")
    canvas.itemconfig(title, text=f"Deutsch", fill="black")
    window.after(3000, func=flip_card)
    canvas.itemconfig(front_image, image=img)


# ---------------------------- FLIP CARDS ------------------------------- #


def flip_card():
    canvas.itemconfig(front_image, image=back_image)
    canvas.itemconfig(word_old, text=f"{word['English']}", fill="white")
    canvas.itemconfig(title, text="English", fill="white")


# print(my_dict[random.randint(0,len(my_dict)-1)]['German'])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Deutsch mit flashcards lernen")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526)
img = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file='images/card_back.png')
front_image = canvas.create_image(400, 267, image=img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_old = canvas.create_text(400, 263, text="",
                              font=("Ariel", 60, "bold"))

# canvas1 = Canvas(width=100, height=100)
# answer_known = PhotoImage(file="images/right.png")
# canvas1.create_image(50,50, image=answer_known)
# canvas1.config(bg=BACKGROUND_COLOR,highlightthickness=0 )
# canvas1.grid(row=2, column=2)
#
# canvas2 = Canvas(width=100, height=100)
# answer_unknown = PhotoImage(file="images/wrong.png")
# canvas2.create_image(50,50, image=answer_unknown)
# canvas2.config(bg=BACKGROUND_COLOR,highlightthickness=0 )
# canvas2.grid(row=2, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=randomize_wrong_cards)
wrong_button.grid(row=1, column=0)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=randomize_right_cards)
right_button.grid(row=1, column=1)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
randomize_wrong_cards()
window.after(3000, func=flip_card)

window.mainloop()
