from turtle import Turtle
from turtle import Screen as tscreen
from score import grid
tur = None


def makesquare (color , width , turtle):
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.end_fill()
    turtle.up()

class snake:
    def __init__(self , x , y , color , width , bgcol , turlte):
        self.x = x
        self.y = y
        self.head = [x , y]
        self.body = [[x , y]]
        self.direction = 'right'
        self.color = color
        self.width = width
        self.bg = bgcol
        self.screen = screen
        self.turtle = turlte
   
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
        self.draw_()

    def draw_(self):
        self.turtle.tracer(0)
        print(self.turtle)
        print(self.turtle.position())   
        self.turtle.up()
        self.turtle.goto(grid[self.head[0]] , grid[self.head[1]])
        makesquare(self.color , self.width , self.turtle)
        self.turtle.goto(grid[self.body[0][0]] , grid[self.body[0][1]])
        makesquare(self.bg , self.width , self.turtle)
        del self.body[0]


if __name__ == '__main__':
    turtle = Turtle()
    turtle.speed('fastest')
    turtle.hideturtle()
    screen = tscreen()
    screen.screensize(600 , 600)
    body = snake(grid[0] , grid[0] , 'green' , 30 , 'white' , turtle)
    body.move()
    print(body.body)
    body.move()
    print(body.body)
    body.move()
    print(body.body)
    screen.exitonclick()