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
        tur.hideturtle()
        tur.penup()
        self.location = tur.goto(foodX, foodY)
        tur.showturtle()
        tur.pendown()


        
apple = Food("square", "red")
apple.teleporting()
sc = tur.Screen()
sc.screensize(600, 600)
sc.bgcolor("black")
sc.exitonclick()