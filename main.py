"""
Tic-Tac-Toe Python Project
Collaborated with Pleffermint
Start date: 2022-10-3
"""
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

window = Tk()
window.title("Tic-Tac-Toe")

# #information
# info = Label(window, text="This is a pineapple",font="NotoSerif-Regular")
# info.grid(columnspan=3,column=0,row=1)


# Given the position of x and y, we will alter the text on the GUI
char_count = 0
def mark_button(x, y):
    global char_count
    # Alternate the char value between X and O
    if char_count % 2 == 0:
        char = "O"
    else:
        char = "X"
    char_count += 1

    # positions[x][y]['font'] = ("Arial", 20)
    positions[x][y]['text'] = char


positions = [
             [],
             [],
             []
            ]

# Creating the tic-tac-toe board
for x in range(3):
    for y in range(3):
        # button = Button(window, bg="#20bebe", fg="white", height=10, width=20, command=lambda a=x, b=y : mark_button(a, b))
        button = Button(window, bg="#20bebe", fg="white", font=("Verdana", 60), width=3, command=lambda a=x, b=y : mark_button(a, b))
        button.grid(row=x, column=y)

        # Saves the button objects to our position list.
        positions[x].append(button)

window.mainloop()