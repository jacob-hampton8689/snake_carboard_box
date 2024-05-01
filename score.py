import turtle as tur
snake_score = 0
high_score = 0
class Score:
  def __init__(self, width, height, color,title):
    self.width = width
    self.height = height
    self.color = color
    self.score = snake_score
    self.all_time_score = high_score
    self.title = title

  
     

  def update_score(self):
     tur.clear()
     tur.write("Score: {} High Score: {} ".format(self.score, self.all_time_score), align="center", font=("arial", 24, "bold"))
     self.score += 10
     self.all_time_score += high_score

  def screen_title(self, title):
     title = tur.title(title)
    
  def screen_elements(self, width, height, color):
     tur.Screen()
     tur.screensize(width, height)
     tur.bgcolor(color)
     tur.speed(0)
     tur.shape('circle')
     tur.color('white')
     tur.penup()
     tur.hideturtle()
     tur.goto(0, 310)
     tur.write("Score: " + str(self.score) + " High score: " + str(self.all_time_score), font= 
    ("Arial", 24, "normal"))
     tur.exitonclick()
    
def test():
   screen = Score(600, 680, "black", "Snake!")
   screen.screen_title(screen.title)
   screen.screen_elements(screen.width, screen.height, screen.color)



if __name__ == '__main__':
   test()