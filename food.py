from score import grid
import turtle as tur
import random as ran


class Food:
    def __init__(self, shape, color , plane):
        shape = tur.shape("square")
        color = tur.color("red")   
        self.shape = shape
        self.color = color
        self.grid = plane

       

    def teleporting(self):
        self.foodY = ran.choice(list(self.grid.keys()))
        self.foodX = ran.choice([self.grid.keys()])
        print(self.grid.keys())
        tur.hideturtle()
        tur.penup()
        '''self.location = tur.goto(self.grid[self.foodX], self.grid[self.foodY])'''
        tur.showturtle()
        tur.pendown()


def test():        
    apple = Food("square", "red" , grid)
    apple.teleporting()
    sc = tur.Screen()
    sc.screensize(600, 600)
    sc.bgcolor("black")
    sc.exitonclick()

if __name__ == '__main__':
    test()
    '''print(foodX)
    print(foodY)
    print(from_x1)
    print(from_x2)'''