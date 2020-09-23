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


def create_rectangle():
    """Create rectangle with given attributes for size, position, and fill"""

    pass


def add_shape():
    """Add a shape. For now, assume rectangle is only shape"""

    start_x, start_y, end_x, end_y, fill_char = get_attributes()


def print_canvas(canvas):
    """Print 10 char x 10 char canvas with any shapes"""

    for row in canvas:
        print("".join(row))


def clear_canvas():
    """Delete all shapes from canvas"""

    pass


def change_rect_fill():
    """Change fill of existing rectangle"""

    pass


def move_rectangle():
    """Move rectangle along x- or y-axis, in positive or negative direction"""

    pass

def main():
    rectangles = {}
    empty_row = [" "] * 10
    canvas = [empty_row] * 10

    action = select_action()

    if action == "1":
        add_shape()

    # print_canvas(canvas)

if __name__ == '__main__':
    main()