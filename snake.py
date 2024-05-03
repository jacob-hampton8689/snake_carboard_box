from turtle import Turtle
from turtle import Screen as tscreen
from score import grid
import time

count = 0

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
        global count
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
        self.collision()
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
        print(count)

    def draw(self):
        screen.tracer(0)  
        self.dood.up()
        print(self.hit_food)
        if self.hit_food == False:
            self.dood.goto(grid[self.body[0][0]] , grid[self.body[0][1]])
            makesquare(self.bg , self.width , self.dood)
            del self.body[0]
        self.dood.goto(grid[self.head[0]] , grid[self.head[1]])
        makesquare(self.color , self.width , self.dood)
        screen.update()

    def collision(self):
        for i in len(self.body):
            if self.body[i + 1] == self.head:
                print('gameover')
             
    def game_over():
        pass

def testmove(snake):
    c = 0
    while c < 3:
        snake.move()
        print(snake.body)
        c += 1
    c = 0
    snake.direction = 'up'
    while c < 5:
        snake.move()
        print(snake.body)
        c += 1
    snake.direction = 'left'
    snake.move()
    snake.direction = 'down'
    snake.move()
    snake.direction = 'right'
    snake.move()

if __name__ == '__main__':
    screen = tscreen()
    dood = Turtle()
    dood.speed('fastest')
    dood.hideturtle()
    screen.screensize(600 , 600)
    body = snake(0 , 0 , 'green' , 30 , 'white' , dood , 5)
    testmove(body)
    screen.exitonclick()