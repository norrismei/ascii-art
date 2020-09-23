from tkinter import *

def create_canvas():
    canvas = Canvas(master, width=600, height=300)
    canvas.pack()

    return canvas

def create_rect(char):
    rect = ""

    for y in range(3):
        for x in range(5):
            rect += char
        rect += "\n"

    return rect

def draw_rectangle(rect):
    canvas.create_text(50, 25, text=rect)

master = Tk()

canvas = create_canvas()

draw = input("Would you like to draw a rectangle? y/n ")

if draw == "y":
    char = input("Enter a character: ")
    rect = create_rect(char)
    draw_rectangle(rect)

mainloop()