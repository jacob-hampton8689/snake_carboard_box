from turtle import Turtle
from turtle import Screen as tscreen
from score import grid
import time

def makesquare (color , width , dood):
    dood.down()
    dood.color(color)
    dood.begin_fill()
    dood.setheading(270)
    dood.forward(width)
    dood.left(90)
    dood.forward(width)
    dood.left(90)
    dood.forward(width)
    dood.left(90)
    dood.forward(width)
    dood.end_fill()
    dood.up()

class snake:
    def __init__(self , x , y , color , width , bgcol , turlte , speed):
        global screen
        self.x = x
        self.y = y
        self.head = [x , y]
        self.body = [[x , y]]
        self.direction = 'right'
        self.color = color
        self.width = width
        self.bg = bgcol
        self.screen = screen
        self.dood = turlte
        self.hit_food = False
        self.speed = speed
   
    def move(self):
        xpos = self.head[0]
        ypos = self.head[1]
        if self.direction == 'right':
            xpos += 1
        if self.direction == 'left':
            xpos -= 1
        if self.direction == 'up':
            ypos += 1
        if self.direction == 'down':
            ypos -= 1
        self.head = [xpos , ypos]
        self.body.append([xpos , ypos])
        self.draw()
        time.sleep(10 / self.speed)

    def draw(self):
        screen.tracer(0)  
        print(self.dood)
        print(self.dood.position())   
        self.dood.up()
        self.dood.goto(grid[self.body[0][0]] , grid[self.body[0][1]])
        makesquare(self.bg , self.width , self.dood)
        self.dood.goto(grid[self.head[0]] , grid[self.head[1]])
        makesquare(self.color , self.width , self.dood)
        if self.hit_food == False:
            del self.body[0]
        screen.update()

    def collision(self):
        for i in self.body:
            if i == self.head:
                print('gameover')
                self.game_over()


    def game_over():
        pass


if __name__ == '__main__':
    screen = tscreen()
    dood = Turtle()
    dood.speed('fastest')
    dood.hideturtle()
    screen.screensize(600 , 600)
    body = snake(grid[0] , grid[0] , 'green' , 30 , 'white' , dood , 5)
    body.move()
    print(body.body)
    body.move()
    print(body.body)
    body.move()
    print(body.body)
    screen.exitonclick()