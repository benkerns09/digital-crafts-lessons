from turtle import *

def draw_square(size = 100):
    for i in range(4):
        forward(100)
        left(90)
    if __name__ == '__main__':
draw_square()

up()#lift the marker up
forward(200)
down()#lift the marker down

draw_square()

mainloop() #will keep window open