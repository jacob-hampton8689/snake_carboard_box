import turtle
import os
os.environ.__setitem__('Display' , ':0.0')
tur = turtle.Turtle()


def screen (x , y , name):
    tur.title(name)
    tur.geometry(f'{x}x{y}')

if __name__ == '__main__':
    screen(600 , 620 , 'snake')
    while True:
        tur.exitonclick