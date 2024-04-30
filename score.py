import turtle as tur


class Score:
    def __init__(self, width, height, score, title):
        self.width = width
        self.height = height
        self.score = score
        self.title = title


    def update_score(self):
        self.score += 1

    def screen_title(title):
        title = tur.title("Snake!")

