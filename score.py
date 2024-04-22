import turtle
tur = turtle.Turtle()
import os


def screen (x , y , name):
    tur.title(name)
    tur.geometry(f'{x}x{y}')

if __name__ == '__main__':
    os.environ.__setitem__('Display' , ':0.0')
    screen(600 , 620 , 'snake')
    while True:
        tur.exitonclick