def create_rectangle():
    """Create rectangle with given attributes for size, position, and fill"""

    pass


def add_shape():
    """Add a shape. For now, assume rectangle is only shape"""

    pass


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


rectangles = {}
empty_row = [" "] * 10
canvas = [empty_row] * 10

print_canvas(canvas)