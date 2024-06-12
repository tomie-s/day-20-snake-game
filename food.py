from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.goto(rand_x, rand_y)
