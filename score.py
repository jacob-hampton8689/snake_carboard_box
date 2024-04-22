import turtle as tur

def screen (x , y , name):
    tur.title(name)
    sc = tur.Screen()
    sc.setup(x,y,startx=0,starty=0)

if __name__ == '__main__':
    screen(600 , 620 , 'snake')
    while True:
        tur.exitonclick