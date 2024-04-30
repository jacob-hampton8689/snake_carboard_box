import turtle as tur


class Score:
  def __init__(self, width, height, color,  score, title):
    self.width = width
    self.height = height
    self.color = color
    self.score = score
    self.title = title


  def update_score(self):
     self.score += 1

  def screen_title(self, title):
     title = tur.title(title)
    
  def screen_elements(self, width, height, color):
     tur.Screen()
     tur.screensize(width, height)
     tur.bgcolor(color)
     tur.exitonclick()
    



screen = Score(600, 600, "black", 0, "Snake!")
screen.screen_title(screen.title)
screen.screen_elements(screen.width, screen.height, screen.color)