import turtle as tur
import score

class snake:
    def __init__(self , x , y):
        self.x = 0
        self.y = 0
        self.head = [x , y]
        self.body = [[x , y]]
        self.direction = 'right'
   
    def move(self):
        self.body.append(self.head)
        if self.direction == 'right':
            self.head[0] += 1
        if self.direction == 'left':
            self.head[0] -= 1
        if self.direction == 'up':
            self.head[1] += 1
        if self.direction == 'down':
            self.head[1] -= 1








if __name__ == '__main__':
    score.test()