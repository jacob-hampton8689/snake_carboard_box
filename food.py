import turtle as tur
import random as ran
from score import grid

foodY = ran.choice(grid.keys())
foodX = ran.choice(grid.keys())

class Food:
    def __init__(self, shape, color):
        shape = tur.shape("square")
        color = tur.color("red")
        self.shape = shape
        self.color = color
        self.posy = foodX
        self.posy = foodY
        self.location = (foodX, foodY)
       

    def teleporting(self):
        tur.hideturtle()
        tur.penup()
        self.location = tur.goto(foodX, foodY)
        tur.showturtle()
        tur.pendown()


def test():        
    apple = Food("square", "red")
    apple.teleporting()
    sc = tur.Screen()
    sc.screensize(600, 600)
    sc.bgcolor("black")
    sc.exitonclick()

if __name__ == '__main__':
    test()
    print(foodX)
    print(foodY)
    print(from_x1)
    print(from_x2)