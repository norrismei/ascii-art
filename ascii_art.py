from tkinter import *

def create_canvas():
    canvas = Canvas(master, width=600, height=300)
    canvas.pack()

    return canvas


def show_option_menu():
    """Prints actions that user can take"""

    print("""
What would you like to do?
1) Draw a rectangle
2) Clear canvas
        """)


def create_rect(char):
    """Creates a string representing rectangle with character as fill"""

    rect = ""

    for y in range(3):
        for x in range(5):
            rect += char
        rect += "\n"

    return rect


def display_rectangle(rect):
    """Takes in string and draws text on canvas"""
    canvas.create_text(50, 25, text=rect)


def draw_rectangle():
    """Asks user for char to use as rectangle fill and displays result"""
    char = input("Enter a character: ")
    rect = create_rect(char)
    display_rectangle(rect)


# Create the GUI window and canvas
master = Tk()
canvas = create_canvas()

while True:
    show_option_menu()
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        draw_rectangle()
    elif choice == "2":
        canvas.delete(ALL)


# Keeps the window open
mainloop()