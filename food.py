import turtle as tur
import random as ran

foodY = ran.randint(-280, 280)
foodX = ran.randint(-280,280)


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
        self.location = tur.goto(foodX, foodY)


        
