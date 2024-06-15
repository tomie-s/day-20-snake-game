from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_box(position)

    def add_box(self, position):
        new_box = Turtle(shape='square')
        new_box.color('white')
        new_box.penup()
        new_box.goto(position)
        self.snake_body.append(new_box)

    def restart(self):
        for box in self.snake_body:
            box.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend_body(self):
        self.add_box(self.snake_body[-1].position())

    def move(self):
        for box_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[box_num - 1].xcor()
            new_y = self.snake_body[box_num - 1].ycor()
            self.snake_body[box_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
