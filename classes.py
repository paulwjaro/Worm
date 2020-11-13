from turtle import Turtle
import random

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_pieces = []
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
            self.add_segment()
            snake = self.snake_pieces[i]
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

    def grow_snake(self):
        self.add_segment()
        snake_size = len(self.snake_pieces)
        snake = self.snake_pieces[snake_size - 1]
        snake.setx(self.snake_pieces[snake_size - 2].xcor())
        snake.sety(self.snake_pieces[snake_size - 2].ycor())

    def add_segment(self):
        snake = Turtle(shape="square")
        snake.color("green")
        snake.penup()
        self.snake_pieces.append(snake)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.75, 0.75)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.x = 0
        self.y = 0
        self.eaten()

    def eaten(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.sety(260)
        self.score = 0

    def display_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.score += 10

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", move=False, align="center", font=("Arial", 24, "normal"))
