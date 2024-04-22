import turtle as tur

def screen (x , y , name):
    tur.title(str(name))
    sc = tur.Screen()
    sc.setup(x,y,startx=0,starty=0)
    return sc

if __name__ == '__main__':
    screen1 = screen(600 , 620 , 'snake')