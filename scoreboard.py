from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, ALIGNMENT, FONT)

    def game_over(self):
        self.color('green')
        self.goto(0, 0)
        self.write('GAME OVER', False, ALIGNMENT, FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
