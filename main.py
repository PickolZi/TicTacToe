"""
Tic-Tac-Toe Python Project
Collaborated with Pleffermint
Start date: 2022-10-3
"""
from tkinter import *
from tkinter import font

# Keeps track of all button objects.
button_positions = [
    [],
    [],
    []
]

# Keeps track of all characters on the board.
char_positions = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# Given the position of x and y, we will alter the text on the GUI
char_count = 0
def mark_button(x, y):
    if winner:
        return

    # Check if the button already has any characters written on the board
    if button_positions[x][y]['text'] != "":
        return

    global char_count
    # Alternate the char value between X and O
    if char_count % 2 == 0:
        char = "O"
    else:
        char = "X"
    char_count += 1

    # Sets the character onto the game board and digital variable board.
    button_positions[x][y]['text'] = char
    char_positions[x][y] = char

    check_winner(char)

    # Changes the display at the top of the screen to present who's turn it is.
    if char == "O":
        display_char_turn("X")
    elif char == "X":
        display_char_turn("O")


def check_winner(char):
    # Checks all Horizontal Rows
    for row in char_positions:
        if row[0] == char and row[1] == char and row[2] == char:
            declare_winner(char)

    # Check all Vertical Columns
    for i in range(len(char_positions)):
        if char_positions[0][i] == char and char_positions[1][i] == char and char_positions[2][i] == char:
            declare_winner(char)

    # Check diagonals
    if char_positions[0][0] == char and char_positions[1][1] == char and char_positions[2][2] == char:
        declare_winner(char)

    if char_positions[0][2] == char and char_positions[1][1] == char and char_positions[2][0] == char:
        declare_winner(char)


def display_char_turn(char):
    if winner:
        return

    player_turn_label['text'] = f"It is now {char}'s turn"


def reset_board():
    global winner
    winner = False

    # Resets all the button object's text to ""
    for row in button_positions:
        for button in row:
            button['text'] = ""

    for x, row in enumerate(char_positions):
        for y, button in enumerate(row):
            char_positions[x][y] = ""


def declare_winner(char):
    global winner
    winner = True

    player_turn_label['text'] = f"{char} is the winner!"
    print("There is a winner!")


# Initializes Tic-Tac-Toe window
window = Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

winner = False

# Adding a label for displaying who's turn it is
player_turn_label = Label(window, text="It is now O's turn", anchor=CENTER, font=("Verdana", 16))
player_turn_label.grid(columnspan=3, pady=10)

# Creating the tic-tac-toe board
for x in range(3):
    for y in range(3):
        button = Button(window, bg="#20bebe", fg="white", font=("Verdana", 60), width=3,
                        command=lambda a=x, b=y: mark_button(a, b))
        button.grid(row=1+x, column=y)

        # Saves the button objects to our position list.
        button_positions[x].append(button)

# Adding a restart button under the board.
restart_button = Button(window, text="Restart", command=reset_board)
restart_button.grid(columnspan=3, pady=10)


window.mainloop()
