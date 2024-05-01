import turtle as tur
snake_score = 0
high_score = 0
grid = {}
for i in range(300):
   if i % 30 == 0:
         grid.update({i // 30 : i})
         grid.update({i // -30 : i * -1})


class Score:
  def __init__(self , width , height , color , title):
    self.width = width
    self.height = height
    self.color = color
    self.score = snake_score
    self.all_time_score = high_score
    self.title = title

  def display_score():
     pen = tur.Turtle()
     pen.speed(0)
     pen.shape('circle')
     pen.color('white')
     pen.penup()
     pen.hideturtle()
     pen.goto(0, 310)
     tur.write("Score: " + str(snake_score) + " High score: " + str(high_score), font= 
    ("Arial", 24, "normal"))
     

  def update_score(self):
     tur.clear()
     tur.write("Score: {} High Score: {} ".format(self.score, self.all_time_score), allign="center", font=("arial", 24, "bold"))
     self.score += 10
     self.all_time_score += high_score

  def screen_title(self, title):
     title = tur.title(title)
    
  def screen_elements(self, width, height, color):
     tur.Screen()
     tur.screensize(width, height)
     tur.bgcolor(color)
     tur.exitonclick()
    
def test():
   screen = Score(600, 680, "black", "Snake!")
   screen.screen_title(screen.title)
   screen.display_score()
   screen.screen_elements(screen.width, screen.height, screen.color)



if __name__ == '__main__':
   '''test()'''
   print(grid)