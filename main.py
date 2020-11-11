from turtle import Screen, Turtle
import time
from classes import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Inch Worm")
screen.tracer(0)
gameon = True
screen.listen()
player = Snake()
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
    screen.update()
    time.sleep(0.1)
    player.move_snake()

screen.bye()
screen.mainloop()
