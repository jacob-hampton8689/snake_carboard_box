import turtle as tur
import random as ran
from score import grid


class Food:
    def __init__(self, shape, color,plane):
        shape = tur.shape("square")
        color = tur.color("red")
        self.shape = shape
        self.color = color
        self.grid = plane
       

    def teleporting(self):
        foodY = ran.choice(list(grid.keys()))
        foodX = ran.choice(list(grid.keys()))
        tur.hideturtle()
        tur.penup()
        self.location = tur.goto(grid[foodX], grid[foodY])
        tur.showturtle()
        tur.pendown()


def test():        
    apple = Food("square", "red", grid)
    apple.teleporting()
    sc = tur.Screen()
    sc.screensize(600, 600)
    sc.bgcolor("black")
    sc.exitonclick()

if __name__ == '__main__':
    test()
    