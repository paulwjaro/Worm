from turtle import Screen
import time
from classes import Snake, Food, Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Inch Worm")
screen.tracer(0)
gameon = True
screen.listen()
player = Snake()
food = Food()
score = Score()
player.build_snake()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")


def end_game():
    global gameon
    gameon = False


screen.onkey(end_game, "q")

while gameon:
    score.clear()
    score.display_score()
    screen.update()
    time.sleep(0.1)
    player.move_snake()

    # collision check
    if player.head.distance(food) <= 20:
        food.eaten()
        score.update_score()
        player.grow_snake()

    # collision with tail
    for i in player.snake_pieces[1:]:
        if player.head.distance(i) <= 10:
            gameon = False

    # detect wall
    if player.head.xcor() > 290 or player.head.xcor() < -300 or player.head.ycor() > 290 or player.head.ycor() < -290:
        gameon = False


food.hideturtle()
score.game_over()

screen.exitonclick()
