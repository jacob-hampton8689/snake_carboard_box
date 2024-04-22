import turtle as tur


def screen (x , y , name):
    sc = tur.Screen()
    sc.setup(x,y,startx=0,starty=0)
    sc.title(name)

if __name__ == '__main__':
    screen(600 , 620 , 'snake')
    while True:
        tur.exitonclick