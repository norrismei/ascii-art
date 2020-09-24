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

    fill_matrix = [[False] * 10 for i in range(10)]

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            # If the coordinates fall outside of matrix/boundary, 
            # characters will not render. Rectangle is effectively cropped.
            try:
                fill_matrix[y][x] = True
            except:
                continue

    return fill_matrix


def add_rect_to_dict(rectangles, fill_matrix, fill_char, 
                     start_x, start_y, end_x, end_y):
    """Add rectangle to rectangles dict"""

    id = len(rectangles) + 1

    rectangles[id] = [fill_char, fill_matrix, [start_x, start_y, end_x, end_y]]

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
    rectangles = add_rect_to_dict(rectangles, fill_matrix, fill_char, 
                                  start_x, start_y, end_x, end_y)
    canvas = update_canvas(canvas, rectangles)
    print_canvas(canvas)


def print_canvas(canvas):
    """Print 10 char x 10 char canvas with any shapes"""

    for row in canvas:
        print("".join(row))


def clear_canvas():
    """Returns canvas with no shapes"""

    #Create a blank 10x10 char matrix. 
    canvas = [[" "] * 10 for i in range(10)]

    return canvas


def clear_rectangles():
    """Returns dictionary with no triangles"""

    return {}


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


def select_axis():

    options = """
Along which axis would you like to move the rectangle?
x-axis (moving left or right)
y-axis (moving up or down)
    """
    print(options)

    return input("Enter x or y: ")


def update_rectangle(rectangles, rectangle, axis, num_spaces):
    """Updates fill_matrix and starting/ending coords of a single rectangle"""

    old_start_x, old_start_y, old_end_x, old_end_y = rectangles[rectangle][2]
    
    if axis == "x":
        start_x = old_start_x + num_spaces
        start_y = old_start_y
        end_x = old_end_x + num_spaces
        end_y = old_end_y

    elif axis == "y":
        start_x = old_start_x
        start_y = old_start_y - num_spaces
        end_x = old_end_x
        end_y = old_end_y - num_spaces

    fill_matrix = get_fill_instructions(start_x, start_y, end_x, end_y)

    rectangles[rectangle][1] = fill_matrix
    rectangles[rectangle][2] = [start_x, start_y, end_x, end_y]

    return rectangles


def move_rectangle(canvas, rectangles):
    """Move rectangle along x- or y-axis, in positive or negative direction"""

    rectangle = select_rectangle(rectangles)
    axis = select_axis()
    num_spaces = int(input(
                 "Move how many spaces? (Use negative num for left or down) "))
    rectangles = update_rectangle(rectangles, rectangle, axis, num_spaces)
    canvas = update_canvas(canvas, rectangles)
    print_canvas(canvas)


def main():
    rectangles = clear_rectangles()

    while True:
        canvas = clear_canvas()

        action = select_action()

        if action == "1":
            add_shape(canvas, rectangles)
        elif action =="2":
            move_rectangle(canvas, rectangles)
        elif action == "3":
            change_rect_fill(canvas, rectangles)
        elif action == "4":
            canvas = clear_canvas()
            rectangles  = clear_rectangles()
            print_canvas(canvas)


if __name__ == '__main__':
    main()