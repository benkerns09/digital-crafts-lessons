def drawtriangle(height, base):
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)
drawtriangle(6, 4)

def box(height, width):
    for row in range(height):
        if row in[0] or row in[(height-1)]:
            print("* " * (width))
        else:
            print("*"+"  "*(width-2)+" *")
box(2, 7)

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