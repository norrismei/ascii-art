def select_action():
    """Show actions menu and return user's input"""

    actions = """
What would you like to do?
1) Draw a rectangle
2) Move rectangle
3) Change rectangle fill
4) Clear canvas
    """

    print(actions)

    return input("Enter number: ")


def get_attributes():
    """Get position and fill for shape"""

    print("Where should the top-left corner of the rectangle be positioned?")
    start_x = int(input("Enter number of column (0-9): "))
    start_y = int(input("Enter number of row (0-9): "))

    print("Where should the bottom right corner of the rectangle be positioned?")
    end_x = int(input("Enter number of column (0-9): "))
    end_y = int(input("Enter number of row (0-9): "))

    fill_char = input("Enter a character to draw the rectangle with: ")

    return start_x, start_y, end_x, end_y, fill_char


def get_fill_instructions(start_x, start_y, end_x, end_y):
    """Returns a matrix where True represents a part of the rectangle"""

    fill_matrix = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False]]

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            fill_matrix[y][x] = True

    return fill_matrix


def add_rect_to_dict(rectangles, fill_matrix, fill_char):
    """Add rectangle to rectangles dict"""

    id = len(rectangles) + 1

    rectangles[id] = [fill_char, fill_matrix]

    return rectangles


def update_canvas(canvas, rectangles):
    """Using fill_matrix instructions, update canvas with fill_char"""

    for rectangle in rectangles:
        fill_char = rectangles[rectangle][0]
        fill_matrix = rectangles[rectangle][1]

        for matrix_row, canvas_row in zip(fill_matrix, canvas):
            for i in range(10):
                if matrix_row[i] == True:
                    canvas_row[i] = fill_char

    return canvas


def add_shape(canvas, rectangles):
    """Add a shape. For now, assume rectangle is only shape"""

    start_x, start_y, end_x, end_y, fill_char = get_attributes()
    fill_matrix = get_fill_instructions(start_x, start_y, end_x, end_y)
    rectangles = add_rect_to_dict(rectangles, fill_matrix, fill_char)
    canvas = update_canvas(canvas, rectangles)
    print_canvas(canvas)


def print_canvas(canvas):
    """Print 10 char x 10 char canvas with any shapes"""

    for row in canvas:
        print("".join(row))


def clear_canvas():
    """Delete all shapes from canvas"""

    canvas = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

    rectangles = {}

    return canvas, rectangles


def select_rectangle(rectangles):
    """Display list of rectangles and return user choice"""

    for rectangle, attributes in rectangles.items():
        num = rectangle
        fill_char = attributes[0]
        print(f"{num}) {fill_char}")

    choice = int(input("Enter number of a rectangle: "))

    return choice


def change_rect_fill(canvas, rectangles):
    """Change fill of existing rectangle"""

    rectangle = select_rectangle(rectangles)
    fill_char = input("Enter a new character: ")
    rectangles[rectangle][0] = fill_char
    canvas = update_canvas(canvas, rectangles)
    print_canvas(canvas)
    

def move_rectangle():
    """Move rectangle along x- or y-axis, in positive or negative direction"""

    pass

def main():
    canvas, rectangles = clear_canvas()

    while True:
        action = select_action()

        if action == "1":
            add_shape(canvas, rectangles)
        elif action == "3":
            change_rect_fill(canvas, rectangles)
        elif action == "4":
            canvas, rectangles = clear_canvas()
            print_canvas(canvas)


if __name__ == '__main__':
    main()