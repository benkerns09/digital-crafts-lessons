def drawsquare(width, height):
    for row in range(height):
        if row == 0:
            print "*" * width
        elif row == height - 1:
            print "*" * width
        else:
            spaces = width - 2
            print "*" + " " * spaces + "*"

drawsquare(10, 5)
drawsquare(50, 5)
