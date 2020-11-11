from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_pieces = []
        self.directions = {}
        self.head = None

    def move_snake(self):
        snake_size = len(self.snake_pieces)
        for part in range(snake_size - 1, 0, -1):
            dx = self.snake_pieces[part - 1].xcor()
            dy = self.snake_pieces[part - 1].ycor()
            self.snake_pieces[part].goto(dx, dy)
        self.snake_pieces[0].forward(20)

    def build_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.color("green")
            snake.penup()
            self.snake_pieces.append(snake)
            snake.goto(START_POSITIONS[i])
        self.head = self.snake_pieces[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


class Food:
    pass


class Score:
    pass
